"""
Author: RL
Date: 2023-03-10
Time: 30 Minutes

Read the Questions and Answer Them as best as you can.
Feel Free to use Previous Notes from Other Lessons.

"???" Fill in the Gaps.
"""
from random import randint, choice
from time import sleep  # https://docs.python.org/3/library/time.html#time.sleep


# Excercise 1
"Write a subroutine that will let the user Input 2 numbers for Ranint(), and prints the result."


def userRandomInput():
    print("Random Number Picker")
    var1 = int(input("Enter an Integer\n"))
    var2 = int(input("Enter a Integer\n"))
    random1 = randint(var1, var2)

    answer = f"Random number from {var1} to {var2}{random1}"

    print(answer)


# userRandomInput()

# Richie's solution
# def userRandomInput():
#     print("Random Number Picker")
#     var1 = int(input("Enter an Integer\n"))
#     var2 = int(input("Enter a Integer\n"))
#     answer = randint(var1, var2)

#     answer = f"Random number from {var1} to {var2}{answer}"

#     print(answer)


# userRandomInput()


# Excercise 2
"Use any randint or otherwise, Pick a random fruit from the basket and print it to the user."

# Complete the Function


def pickFruit():
    ListA = ["Banana", "Apples", "Oranges", "Melon", "Pears"]

    # finish the code
    result = choice(ListA)
    print(result)


# pickFruit()

# # Richie's solution

# def pickFruit():
#     ListA = ["Banana", "Apples", "Oranges", "Melon", "Pears"]

#     # finish the code
# 		# Richie's solution 1
#     selection = randint(0, len(ListA) - 1)
#     print(ListA[selection])
#     # second solution
#     print(choice(ListA))

# pickFruit()


# Excercise 3
"Complete the following code in order to build a Menu function"
"Uncomment the Code to Begin:"


def menu():
    menuUI = '''
	Please Select an Option Below:
	1. Generate a Random Number
	2. Pick A Fruit
	3. Log Off (Exit)
	'''
    print(menuUI)
    options = ["1", "2", "3"]
    userChoice = ""
    while userChoice not in options:
        userChoice = input("Select an option from the menu: ")
        if userChoice not in options:
            print(userChoice, "isnt a valid option.")
            sleep(0.5)
    return userChoice


# print(menu())


# Excercise 4
"Turn the following code into a subroutine called login()"
"Uncomment the Code to Begin:"


def login():
    passcode = "pass123"
    userInput = input("Enter the passcode: ")
    while userInput != passcode:
        userInput = input("Wrong, Try again: ")

    print("access granted")
    sleep(2)


# Excercise 5
"!!! This Excercises Uses all the functions from Excercise 1, 2, 3 and 4. Ensure that they work in order to proceed here !!!"

"Complete the code in order to build a Basic command line interface"
"Un-comment the code to begin the excercise"

OPERATINGSYSTEM = "BasicPyOS"


def greet():
    name = input("Enter your Name: ")
    print(f"\nHello {name}, Welcome to {OPERATINGSYSTEM}")
    sleep(1.5)  # notice the sleep function


def computer():
    greet()
    login()
    menuChoice = menu()
    if menuChoice == 1:
        userRandomInput()
    elif menuChoice == 2:
        pickFruit
    else:
        print("Exiting/logging off")


computer()
