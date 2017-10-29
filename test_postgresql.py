import psycopg2
import sys


def main():
    # Define our connection string
    # conn_string = "host='localhost' dbname='ftest1' user='postgres' password='root'"
    conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"
    # conn_string = "host='awd' dbname='awd' user='awd' password='awd'"
    # print the connection string we will use to connect
    print("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")

#     cursor.execute("""SELECT
#  *
# FROM
#  pg_catalog.pg_tables
# WHERE
#  schemaname != 'pg_catalog'
# AND schemaname != 'information_schema';""")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    print([el[0] for el in cursor.fetchall()])

    for table in cursor.fetchall():
        print(table)

    # cursor.execute("select * from sc.table;")
    # print(cursor.fetchall())



    # cursor.execute("select * from person;")
    # print(cursor.fetchone())

    cursor.close()
    conn.close()
















if __name__ == "__main__":
    main()