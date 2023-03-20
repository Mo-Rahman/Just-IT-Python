from connect1 import *
from time import sleep
# read


def read():
    sqlcode = "SELECT * FROM songs"
    cursor.execute(sqlcode)

    # Grab the data from teh latest query
    results = cursor.fetchall()
    # print(results)
    # Extract each row (tuple) and print them line by line.
    print("\nSongs List")
    for row in results:
        print(row)
    sleep(2)


if __name__ == "__main__":
    read()
