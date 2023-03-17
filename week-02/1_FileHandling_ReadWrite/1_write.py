"Spend 3 minutes to read the comments"

"""
Session objectives
●   Use context manager to handle resource usage
●	Write to text files
●	Read data from a text file
●	Append to text files

Key vocabulary
Data files, text files
"""
# In order to read the data stored in a text file, you must open it first. ​

# Just like a book. You can’t read what is inside if you don’t open it first.​

# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files

"""
Key file-handling techniques are:Open, Read ,Close, Write, Append
The text file must be saved in the same location as your Python file for the program to work. 
"""

"1_FileHandling_ReadWrite/myfile.txt", "w"
"Syntax :  varName = openMethod('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'w')"
# userFile= open("1_FileHandling_ReadWriteStartFiles/file1.txt", "w") # folder/folder/filename
# 1_FileHandling_ReadWrite

# userFile = open("1_FileHandling_ReadWrite/file1.txt",
#                 "w")  # folder/folder/filename
# userFile.write("This is Python\nProgramming\nwriting to text files")
# # userFile.write("This is a test")
# userFile.close()

# Context Manager: "w" writes to a file and overwrites exisiting files.
with open("1_FileHandling_ReadWrite/file2.txt", "w") as userFile2:
    contents = "Using context manager"
    userFile2.write(contents)


"To Do: Task1: Create a file called yourName.txt and Write your name to the file"
# If stuck refer to the example above
"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html
