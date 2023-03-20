from connect1 import *
from time import sleep
from readSongs import read

# Create a function


def insertSongs():
    # create a empty list
    songs = []

    # Ask for user input for SongID, Title, Artist and Genre
    # SongID is not required because SQLite3 automatically add primary key fields.
    title = input("Enter Song title: ")
    artist = input("Enter Song Artist: ")
    genre = input("Enter Song Genre: ")

    # Append data to songs list.
    songs.append(title)
    songs.append(artist)
    songs.append(genre)

    cursor.execute("INSERT INTO songs VALUES(NULL, ?, ?, ?)", songs)
    conn.commit()  # make the change

    print(f"{title} added to songs table")
    # 2 second delay
    sleep(2)
    read()

    # Delay for three seconds then read from the database.
if __name__ == "__main__":
    insertSongs()
