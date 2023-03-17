# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files


"To Do: Task 1: Modify the code below to"
# Read the contents from your file (yourName.txt) and write to your file by replacing the "w" mode after the file path
# with the correct mode and ensure you use both the read and the write() methods to perform their respective
# operations


with open("1_FileHandling_ReadWrite/file3.txt", "r+") as File3:
    readContents = File3.read()
    print(readContents)
    contents = "\nUsing context manager"
    File3.write(contents)
