from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets

import psycopg2
from psycopg2.extensions import AsIs
import sys



class ConnectionDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):

        QtWidgets.QDialog.__init__(self)
        self.dialog_window = loadUi("dialog.ui")
        self.buttonBox = self.dialog_window.buttonBox
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.reject)
        self.conn_string = ""



    def apply(self):
        conn_string = str("host='"+self.dialog_window.lineEdit_5.text()+"' dbname='"+self.dialog_window.lineEdit_6.text()+"' user='"+self.dialog_window.lineEdit_7.text()+"' password='"+self.dialog_window.lineEdit_9.text()+"'")

        if self.test_connection(conn_string):
            self.conn_string = conn_string




        else:
            QMessageBox.information(self.dialog_window, 'INFO', "Please check the connection data or existence of database.",
                                 QMessageBox.Ok)
            self.dialog_window.show()


    def reject(self):
        sys.exit()

    def test_connection(self,conn_string):
        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.close()
            conn.close()
            return True
        except Exception :
            QMessageBox.critical(self.dialog_window, 'ERROR', "Error during connection to database.",
                                 QMessageBox.Ok)
            return False




class DdWindow( QtWidgets.QMainWindow):

    def __init__(self, cn_string, parent=None):
        self.flag = True
        self.choosen_schema = None
        self.choosen_table = None
        QtWidgets.QMainWindow.__init__(self)
        self.init_connection(cn_string)
        self.main_window = loadUi("mwindow.ui")
        self.main_table = self.main_window.tableWidget
        self.add_button = self.main_window.add
        self.delete_button = self.main_window.my_delete
        self.search_button = self.main_window.search
        self.help_button = self.main_window.help
        self.table_chooser = self.main_window.table_chooser
        self.schema_chooser = self.main_window.schema_chooser

        self.init_schema_chooser(self.schema_chooser)
        self.init_table_chooser(self.table_chooser)
        self.main()
        # self.fill_table()



    def init_table_chooser(self,tb_chooser):

        try:

            self.cursor.execute(("SELECT TABLE_NAME  from information_schema.tables where table_schema= '{0}'").format(
                self.choosen_schema))

        except Exception as e:
            print(e)

        table_names = [name[0] for name in self.cursor.fetchall()]
        # print("AAAAAAAA",table_names)
        if len(table_names) == 0:
            tb_chooser.addItem(str(None))
        else:
            for table in table_names:
                tb_chooser.addItem(table)

            self.choosen_table = self.table_chooser.currentText()
            self.fill_table()


    def clean_table(self):
        self.main_table.setRowCount(0)
        self.main_table.setColumnCount(0)
        self.main_table.clear()

        # self.main_table.setHorizontalHeaderLabels([])




    def init_schema_chooser(self, sh_chooser):
        self.cursor.execute("select schema_name from information_schema.schemata where  schema_name !~ '^(pg_|sql_)'  AND  schema_name !~'information_schema';")
        schema_names = [name[0] for name in self.cursor.fetchall()]
        for schema in schema_names:
            sh_chooser.addItem(schema)
        # sh_chooser.addItem(schema_names[1])

        self.choosen_schema = self.schema_chooser.currentText()

        # sh_chooser.activated.connect(self.init_table_chooser)

    def init_connection(self,conn_string):
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()


    def fill_table(self):

        if self.choosen_schema != None and self.choosen_table != None:

            self.cursor.execute(("SELECT * FROM {0}.{1} ").format(self.choosen_schema, self.choosen_table))
            colnames = [desc[0] for desc in self.cursor.description]
            self.cursor.execute(("SELECT * FROM {0}.{1} ORDER BY  {2}").format(self.choosen_schema, self.choosen_table,colnames[0]))



            # print(self.cursor.description)

            a = self.cursor.fetchall()
            # print( a)

            colnames = [desc[0] for desc in self.cursor.description]

            self.main_table.setColumnCount(len(colnames))

            for n, meaning in  enumerate(a):
                self.main_table.insertRow(self.main_table.rowCount())
                # print(n,"  ",meaning)
                for m, item in enumerate(meaning):
                    # print("\t",m, "  ", item)
                    newitem = QTableWidgetItem(str(item))
                    self.main_table.setItem(n, m, newitem)
                    self.main_table.item(n, m).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.main_table.setHorizontalHeaderLabels(colnames)
            header = self.main_table.horizontalHeader()
            for i in range(header.count()):
                self.main_table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        else:
            print("Nooooo data")


    def main(self):

        self.schema_chooser.activated.connect(self.control_shema_changes)
        self.table_chooser.activated.connect(self.control_table_changes)
        self.add_button.clicked.connect(self.add_record)
        self.delete_button.clicked.connect(self.delete_record)
        self.search_button.clicked.connect(self.search_record)


    def control_shema_changes(self):
        self.choosen_schema = self.schema_chooser.currentText()
        self.table_chooser.clear()
        self.clean_table()
        self.init_table_chooser(self.table_chooser)

    def control_table_changes(self):
        self.choosen_table = self.table_chooser.currentText()
        self.clean_table()
        self.fill_table()

    def add_record(self):


        # import time
        # app2 = QApplication(sys.argv)
        # add = AddDialog(self)
        try:
            add = AddDialog(self)
            add.add_window.exec_()
        except Exception as e:

            QMessageBox.critical(self.main_window, 'ERROR', "No attributes to add data.",
                                 QMessageBox.Ok)



        # app2.exec_()

    def delete_record(self):
        try:
            indexes = [index.row() for index in self.main_table.selectedIndexes()]
            for el in reversed(indexes):
                data = [self.main_table.item(el,i).text().strip() for i in range(self.main_table.columnCount())]
                colnames = [desc[0] for desc in self.cursor.description]
                insert_statement = ("delete from {0}.{1} WHERE  {2} = '{3}';").format(self.choosen_schema,self.choosen_table,colnames[0],data[0])
                self.cursor.execute(insert_statement)
                self.main_table.removeRow(el)
            # data = self.main_table.item(indexes[0],2).text()
            #     print(data)
            # print(indexes)
            # for index in reversed(indexes):
            #     self.main_table.removeRow(index)
        except Exception as e:
            print(e)

    def search_record(self):
        try:
            add = AddDialog(self)
            add.add_window.exec_()
        except Exception as e:

            QMessageBox.critical(self.main_window, 'ERROR', "No attributes to add data.",
                                 QMessageBox.Ok)


class AddDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.add_window = loadUi("test_add.ui")
        self.grid = self.add_window.gridLayout
        self.parent = parent
        self.buttonBox = self.add_window.buttonBox
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.reject)


        try:
            self.form_grid(self.grid, self.parent)
        except psycopg2.Error as e:
            raise psycopg2.Error
        # self.add_window.exec_()



    def form_grid(self,grid,parent):

        try:
            # print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            parent.cursor.execute("""SELECT
                            tc.constraint_name, tc.table_name, kcu.column_name,
                            ccu.table_name AS foreign_table_name,
                            ccu.column_name AS foreign_column_name
                        FROM
                            information_schema.table_constraints AS tc
                            JOIN information_schema.key_column_usage AS kcu
                              ON tc.constraint_name = kcu.constraint_name
                            JOIN information_schema.constraint_column_usage AS ccu
                              ON ccu.constraint_name = tc.constraint_name
                        WHERE constraint_type = 'FOREIGN KEY' AND tc.table_name='{0}';""".format(parent.choosen_table))
            foreign_keys =parent.cursor.fetchall()
            # print(foreign_keys)
            # print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

            parent.cursor.execute(("SELECT * FROM {0}.{1}").format(parent.choosen_schema, parent.choosen_table))
            # print(parent.cursor.description)


        except psycopg2.Error as e:
            parent.conn.rollback()
            print(e)

            #Add rollback to all query !

            raise psycopg2.Error



         # where table_name = 'config';
        # print(parent.cursor.)


        a = parent.cursor.fetchall()
        # print( a)
        # try:
        #     parent.cursor.execute(
        #             (" select column_name, data_type from information_schema.columns where table_name = {0};").format(
        #                 parent.choosen_table))
        #     print("BBBBBBBBBBBBBBB")
        #     print(parent.cursor.fetchall())
        # except psycopg2.Error as e:
        #     # parent.conn.rollback()
        #     pass
        try:
            key_columns = [el[2] for el in foreign_keys]
        except Exception as e:
            print(e)
        # print("DDD ",key_columns)
        colnames = [desc[0] for desc in parent.cursor.description]
        self.dict_of_widgets = {}
        try:
            parent.cursor.execute((" select column_name, data_type from information_schema.columns where table_name = '{0}';").format(
                            parent.choosen_table))
        except Exception as e:
            print(e)
        # print("BBBBBBBBBBBBBBB")
        # print(parent.cursor.fetchall())

        for i in range(len(colnames)):
            if not colnames[i] in key_columns:
                buff_label = QtWidgets.QLabel(colnames[i])
                buff_widget = QtWidgets.QLineEdit()
                grid.addWidget(buff_label, i, 0)
                grid.addWidget(buff_widget, i, 1)
                self.dict_of_widgets[buff_label] = buff_widget
            else:
                index = key_columns.index(colnames[i])
                buff_label = QtWidgets.QLabel(colnames[i])
                buff_widget = QtWidgets.QComboBox()
                try:
                    ins = " select {0} from  {1}.{2};".format(foreign_keys[index][4],parent.choosen_schema,foreign_keys[index][3])
                    # print(ins)
                    parent.cursor.execute((" select {0} from  {1}.{2};").format(foreign_keys[index][4],parent.choosen_schema,foreign_keys[index][3]))
                    rez = parent.cursor.fetchall()
                    # print(rez)
                    for name in rez:
                        buff_widget.addItem(str(name[0]))
                except Exception as e:
                    print("ZZ ",e)


                grid.addWidget(buff_label, i, 0)
                grid.addWidget(buff_widget, i, 1)
                self.dict_of_widgets[buff_label] = buff_widget

        # print(self.dict_of_widgets)
        # for el in self.dict_of_widgets.keys():
        #     print(el.text())


    def apply(self):
        # print(self.dict_of_widgets)
        # for label in self.dict_of_widgets.keys():
        #     print(label.text(),"         ",self.dict_of_widgets[label].text())

        try:
            # for label in self.dict_of_widgets.keys():
            #     # self.parent.cursor.execute(("INSERT INTO {0} ({1}) VALUES ({2});",format(self.parent.choosen_table,label.text(),self.dict_of_widgets[label].text() )))
            #
            #     self.parent.cursor.execute(
            #         ("INSERT INTO {0}.{1} ({2}) VALUES ({3});").format(self.parent.choosen_schema,
            #             self.parent.choosen_table, label.text(), self.dict_of_widgets[label].text()))

            columns = self.dict_of_widgets.keys()
            final_values = [self.dict_of_widgets[column] for column in columns]
            columns = [el.text() for el in columns]

            values= []
            for val in final_values:
                if type(val) == QtWidgets.QLineEdit:
                    values.append(val.text())
                elif type(val) == QtWidgets.QComboBox:
                    values.append(val.currentText())

            # values= [el.text() for el in values]
            print(columns)
            print("VALUES")
            print(values)
            for i in range(len(columns)):
                columns[i] = '"' + columns[i] + '"'
            insert_statement = ('insert into {0}.{1} (%s) values %s'.format(self.parent.choosen_schema,self.parent.choosen_table))
            my_query = self.parent.cursor.mogrify(insert_statement, (AsIs(','.join(columns)), tuple(values)))
            print(my_query)
            self.parent.cursor.execute(my_query)
            self.parent.conn.commit()

        except Exception as e:

            print("ERROR")
            print("----------------------------------------------------------------------")
            print(e)
            QMessageBox.critical(self.add_window, 'ERROR',str(e.diag.message_primary),
                                 QMessageBox.Ok)

    def reject(self):
        pass


class SearchWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.search_window = loadUi("search_dialog.ui")
        self.grid = self.search_window.gridLayout
        self.parent = parent
        self.buttonBox = self.add_window.buttonBox
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.reject)


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = DdWindows()
    # window.open()
    # window.show()
    app = QApplication(sys.argv)
    # test = ConnectionDialog()
    # test.dialog_window.exec_()
    #
    #
    # if test.conn_string!="":
    #     window = DdWindow(test.conn_string)
    #     window.main_window.show()
    # conn_string = "host='localhost'dbname='postgres' user='postgres' password='root'"
    conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"

    if conn_string!="":
        window = DdWindow(conn_string)
        window.main_window.show()


            # app2 = QApplication(sys.argv)

    sys.exit(app.exec_())

