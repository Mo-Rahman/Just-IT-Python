import sqlite3 as sql  # import the sqlite3 module

try:
    # Use the sqlite3 module to create a database and connection to the database.
    connection = sql.connect("DFE555.db")
    # create a curser object and call it execute() method to perform SQL queries.

    cursor = connection.cursor()
    print(connection.total_changes)
except sql.OperationalError as e:
    print(f"Connection failed: {e}")
    # print(conn.total_changes)

# import sqlite3

# connection = sqlite3.connect("")
