
"To Do: Task1:Modify the code below to:"
# Read the contents of your file (yourName.txt) by replacing the "w" mode after the file path
# Then replace the write() method with the read method()

# with open("1_FileHandling_ReadWrite/file2.txt", "w") as userFile2:
#     contents = "Using context manager"
#     userFile2.write(contents)

# split lines
with open('1_FileHandling_ReadWrite/file1.txt', 'r') as file:
    data = file.read().splitlines()
    print(data)

# readlines
with open('1_FileHandling_ReadWrite/file1.txt', 'r') as file:
    read_lines = file.read()
    print(read_lines)

# with open('1_FileHandling_ReadWrite/file1.txt', 'r') as file:
#     data = file.read().splitlines()
#     print(data)
#     read_lines = file.readlines()
#     print(read_lines)
"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html
