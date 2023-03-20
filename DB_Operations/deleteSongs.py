from connect1 import *
from readSongs import read


def delete():
    sure = False
    while sure == False:

        songID = input("Enter the ID of the song you'd like to delete ")
        confirm = input("Are you sure 'y' or 'n' ? ").lower()

        if confirm == "y" or confirm == "yes":
            sure = True

    deleteSQL = f"DELETE from songs WHERE SongID = {songID}"
    cursor.execute(deleteSQL)
    conn.commit()

    print(f"Song ID {songID} has been successfully deleted.")


if __name__ == "__main__":
    delete()
