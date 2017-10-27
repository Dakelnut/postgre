import psycopg2
# conn_string = "host='localhost' user='postgres' password='root'"
# Connect to an existing database
conn_string = "host='localhost'dbname='test38' user='postgres' password='root'"
conn = psycopg2.connect(conn_string)

# Open a cursor to perform database operations
cur = conn.cursor()
#lol kek cheburek
# Execute a command: this creates a new table
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
#       (100, "abc'def"))

# Query the database and obtain data as Python objects
# cur.execute("SELECT name FROM sc.table;")
# for el in cur.fetchall():
#     print(el)
#
# cur.execute("INSERT INTO sc.table (name) VALUES ('name_of_awd');")


cur.execute("SELECT * FROM sc.table;")
for el in cur.fetchall():
    print(el)
# (1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()