
# a for adding to an existing file​ and creates the file if it does not exists
# Using context manager to handling resource usage
" automatically setup and teardown resources"

# open('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', "a")
# filePath.write("\nI Love coding in python and JavasScript") # write to file

"To Do: Task 1: Use the context manager to append to your file (yourName.txt) "
# Append your interests and a fake address

# Context Manager

with open("1_FileHandling_ReadWrite/file3.txt", "w") as userFile3:
    contents = "Using context manager\n"
    userFile3.write(contents)

# Appending to a file
with open("1_FileHandling_ReadWrite/file3.txt", "a") as userFile3:
    contents = "Editing the content using context manager"
    userFile3.write(contents)
"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html
