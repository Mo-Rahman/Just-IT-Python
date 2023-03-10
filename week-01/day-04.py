# Day 4 - If statements

# # Boolean

# x = 50

# print(x > 10)  # True
# print(x == 10)  # False


# If Statement Syntax

# if condtion:
#   # do something
#   # do something
# else:
#     # do something else

# if x > 10:
#     print("Hello World")

# if / else syntax

# if conditon:
#     # Do something
# else:
#     # Do something else

# y = 100

# if y == 10:
#     print("tree")
# else:
#     print("Car")

# if / elif / else syntax

"""
if condition:
    do something
elif condition:
    do something
else:
    do final thing
"""

# z = -120

# if z > 0:
#     print("Z is positive")
# elif z == 0:
#     print("Z is equal to zero")
# else:
#     print("Z is a negative number")


# Iteration

"""
For loops - Definate 
While loops - Indefinate


for number in range():
    do something

for element in collection:
    do something

"""
# # range 0 - 9 exclusive of 10.
# for i in range(10):  # range: 0 - 9
#     print(i)
#     print("Hello world")
# # range from 1 to 9 - start, end.
# for i in range(1, 10):  # range: 01 - 09
#     print(i)
#     print("Hello world")

# # start, end, step.
# for i in range(0, 10, 2):  # range: 02 - 08
#     print(i)
#     print("Hello world")

# for i in collection

fruits = ["apples", "bananas", "pears"]

for fruit in fruits:
    print(fruit)

# basket = fruits

# basket.remove("pears")
# print(basket)
# print(fruits)

# While loops
"""
While loops "Requires a condition of True to run." 
"""

# # A while loop that will run once.
# game_is_running = False

# while not game_is_running:
#     print("Hello world while loop")
#     game_is_running = True


# # A while loop that will run until the condition is met.
# count = 0

# while count < 5:
#     print("Hello world loop")
#     count += 1

# # break statement - will loop once and break out of the loop.
# count = 1
# while count < 2:
#     print("Hello world loop break?")
#     count += 1
#     break


# ### Excercise 1
# "Given the Variable age, Depending on its value, using if statements, tell the user that they are of legal driving age or not."
age = int(input("Enter age"))

if age < 17:
    print("Too young to drive.")
else:
    print("You are of driving age.")


# ### Excercise 2
# "Grading System"
# "Let the user Input their score. Grade the score and print their grade based on the following criteria "
# """
# Grade A: Score 800 or more
# Grade B: Score 600 or more
# Grade C: Score 400 or more
# Grade D: Score 200 or more
# Fail: Scores Under 200
# """

# score = int(input("Please enter your score for a grade\n"))

# if score >= 800:
#     print("Grade A")
# elif score >= 600:
#     print("Grade: B")
# elif score >= 400:
#     print("Grade C")
# elif score >= 200:
#     print("Grade D")
# else:
#     print("Failed")

# Richie's solution with 1 final print.

# score = int(input("Please enter your score for a grade\n"))
# grade = ""
# if score >= 800:
#     grade = "A"
# elif score >= 600:
#     grade = "B"
# elif score >= 400:
#     grade = "C"
# elif score >= 200:
#     grade = "D"
# else:
#     grade = "F"
# print(f"Your final grade is {grade}")

# ### Excercise 3
# "Create a list with a sequence of the first 20 Sqaure Numbers (x ^2)"

times_list = []
for i in range(0, 20):
    times_list.append(i * 2)
print(times_list)
print(len(times_list))

# for i in range(1, 21):
#     print(i*i)

# ### Excercise 4
# "Create a program that will ask the user to guess a passcode."
# "If incorrect, The user must keep on guessing until their input matches the passcode, granting access when correct."

# count = 0
# password = "hello"
# correct = False

# while not correct:
#     guess = input("Guess password\n")
#     if password == guess:
#         correct = True
#         print(f"You guessed the password: {password}")
#     else:
#         correct = False
#         print(f"Incorrect Guess {guess}")
#         count += 1
#         if count >= 3:
#             correct = True
#             print(f"You guessed {count} times\nTo many incorrect guesses")


# passcode = "123456789"
# guess = input("Enter Password")
# # if the guess is not correct the while loop never happens.
# while guess != passcode:
#     guess = input("Invalid password")

# print("Access granted")
