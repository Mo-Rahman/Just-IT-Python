from connect1 import *
from readSongs import read

# Updating rows in SQL
read()


def update():
    songID = input("Enter the ID of the song to update ")

    title = input("Enter new Song title: ")
    artist = input("Enter new Song Artist: ")
    genre = input("Enter new Song Genre: ")

    updateSQL = f"""
    UPDATE songs
    SET Title = "{title}", Artist = "{artist}", Genre = "{genre}"
    WHERE SongID = "{songID}";
    """

    cursor.execute(updateSQL)
    conn.commit()


if __name__ == "__main__":
    update()
