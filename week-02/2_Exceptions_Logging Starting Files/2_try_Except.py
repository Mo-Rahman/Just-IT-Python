
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


# # follow along
# # ZeroDivisionError
# try:  # execute the code within it's block
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter your second number: "))
#     answer = num1 / num2
# except ZeroDivisionError:  # execute if the code failed
#     print("You can't divide by zero")
# except ValueError:  # execute if the code failed
#     print("You can't divide by zero")
# else:  # execute if there is no exception
#     print(f"The answer to {num1} / {num2} = {answer}")
# finally:  # Executes regardless of an exception or not.
#     print("Closing app.")


# A combination of multiple unrelated exceptions.
# ZeroDivisionError, IndentationError, IndexError])
try:
    raise ExceptionGroup("group", [ValueError(124), TypeError])
except ExceptionGroup as errorGroup:
    for err in errorGroup:
        if isinstance(err, ValueError):
            print("Handle Exception group")
        elif isinstance(err, ZeroDivisionError):
            print("Some message")

try:
    raise ExceptionGroup("group", [ValueError(124)])
except* ValueError:
    print("Handle Exception group")
except* TypeError:
    print("Some message")

try:
    raise ExceptionGroup("group", [ValueError(
        123), TypeError("str"), TypeError(int)])
except* ValueError as errorGroup:
    print(f"Handle Exception group {errorGroup.exceptions}")
except* TypeError as errorGroup:
    print(f"Some message {errorGroup.exceptions}")
