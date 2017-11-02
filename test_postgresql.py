import psycopg2
import sys


# def main():
#     # Define our connection string
#     # conn_string = "host='localhost' dbname='ftest1' user='postgres' password='root'"
#     conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"
#     # conn_string = "host='awd' dbname='awd' user='awd' password='awd'"
#     # print the connection string we will use to connect
#     print("Connecting to database\n	->%s" % (conn_string))
#
#     # get a connection, if a connect cannot be made an exception will be raised here
#     conn = psycopg2.connect(conn_string)
#
#     # conn.cursor will return a cursor object, you can use this cursor to perform queries
#     cursor = conn.cursor()
#     print("Connected!\n")
#
# #     cursor.execute("""SELECT
# #  *
# # FROM
# #  pg_catalog.pg_tables
# # WHERE
# #  schemaname != 'pg_catalog'
# # AND schemaname != 'information_schema';""")
#     conn = psycopg2.connect(conn_string)
#     cursor = conn.cursor()
#     cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
#     print([el[0] for el in cursor.fetchall()])
#
#     for table in cursor.fetchall():
#         print(table)
#
#     # cursor.execute("select * from sc.table;")
#     # print(cursor.fetchall())
#
#
#
#     # cursor.execute("select * from person;")
#     # print(cursor.fetchone())
#
#     cursor.close()
#     conn.close()





def main():
    conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    # insert_statement = "insert into sc.table (name) values ('{0}')".format("test_name2")

    # from psycopg2.extensions import AsIs
    # columns = ["name","some_num"]
    # values = ["31","Wwww","4","123443","0.12342","479263"]
    # cursor.execute("Select * from cartel.equipment;")
    # columns = [desc[0] for desc in cursor.description]
    # print(columns)
    # for i in range(len(columns)):
    #     columns[i] = '"'+columns[i] + '"'
    # insert_statement = ('insert into cartel.equipment (inventory_key,"name ","type_of_equipment ",cost,run_out,belongs_to_lab) values {0}').format(tuple(values))
    # print(insert_statement)

    # sta = cursor.mogrify(insert_statement, (AsIs( tuple(values))))
    # sta = cursor.mogrify(insert_statement, (AsIs(','.join(columns)), tuple(values)))
    # print(sta)
    # cursor.execute(insert_statement)

    # self.parent.conn.commit()

    insert_statement = ("select * from sc.pyqt_table where name LIKE  '%est%';")


    cursor.execute(insert_statement)
    print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()