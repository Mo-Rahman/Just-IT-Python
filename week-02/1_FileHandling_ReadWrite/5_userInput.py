fname = input("Enter you full name: ")
address = input("Enter your address: ")
interest = input("Enter your interest: ")
age = int(input("Enter your age: "))

"Make"
"To Do: Task 1: use the code above to ask for user input and then save it to a file called userDetails.txt"

with open("1_FileHandling_ReadWrite/file4.txt", "a") as file:
    # contents = "Using context manager"
    file.write(f"{fname}\n")
    file.write(f"{address}\n")
    file.write(f"{interest}\n")
    file.write(f"{age}\n")
    # Methond 1 using an f-string
    file.write(f"{fname} {address} {interest} {age}\n")
    # Method 2 - concatenation.
    file.write(fname + " " + address + " " + str(age))

"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp
