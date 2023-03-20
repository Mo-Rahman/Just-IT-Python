import sqlite3 as sql  # import the sqlite3 module

# To use the module, start by creating a database Connection object:
# try:
#     # use the sqlite 3 module to create a database and a connection to the database (create a connection object)
try:
    with sql.connect("DB_Operations/DFE5.db") as conn:
        #     # Once a connection has been established,
        #     # create a Cursor object and call its execute() method to perform SQL queries
        cursor = conn.cursor()
except sql.OperationalError as e:
    print(f"Connection failed: {e}")
