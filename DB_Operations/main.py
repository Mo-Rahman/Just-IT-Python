# Main Menu

# Build a menu that lets the user access each of the database operations. (CRUD)

from addSongs import insertSongs
from readSongs import read
from updateSongs import update
from deleteSongs import delete


def menu():
    menuUI = """
    Welcome to DFE5 Music Database v1.32 Beta
        1. Display the songs in teh database...
        2. Add a new song to the database...
        3. Update an existing song...
        4. Delete a specified song...
        5. Exit Application
    """

    choice = ""
    options = ["1", "2", "3", "4", "5"]
    print(menuUI)
    while choice not in options:
        choice = input("Please select an option from the menu: ")
        if choice not in options:
            print("Invalid choice")

    return choice


# print("Pass")
# menu()

# if the user chose 1, - Display the songs using the read() function
# if the user chose 2, - add a new song using insertSongs()
# if the user chose 3, Update a song update()
# if the user chose 4, delete a song delete()

mainMenu = True
while mainMenu:
    userChoice = menu()
    if userChoice == "1":
        read()
    elif userChoice == "2":
        insertSongs()
    elif userChoice == "3":
        update()
    elif userChoice == "4":
        delete()
    else:
        mainMenu = False

# End of the code.
print("Exit Application: Thanks for using the database. ")
