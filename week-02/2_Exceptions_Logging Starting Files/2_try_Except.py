
# num1 = int(input(("Enter your first number: ")))
# num2 = int(input(("Enter your second number: ")))
# answer = num1 / num2
# print(answer)

# print("Execute some code................................")
# print("Execute some code................................")
# print("Execute some code................................")
# print("Execute some code................................")

# try:  # attempt to run the indented code block
#     num1 = int(input(("Enter your first number: ")))
#     num2 = int(input(("Enter your second number: ")))
#     answer = num1 / num2

# except ZeroDivisionError:  # handles exception if code in try block fails
#     print("You can't divide a number by zero")

# else:
#     #Output for user/what the user see
#     print(f"The answer to {num1} / {num2} = {answer}")

# finally:
#     print("Closing....")


# "To Do: Task 1: Modify"
# # Make:
# # 1. Use any other two logging methods to log error to the Exceptions folder in a file called myFilelog1.log


# follow along
# ZeroDivisionError
try:  # execute the code within it's block
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 / num2
except ZeroDivisionError:  # execute if the code failed
    print("You can't divide by zero")
else:  # execute if there is no exception
    print(f"The answer to {num1} / {num2} = {answer}")
finally:  # Executes regardless of an exception or not.
    print("Closing app.")
