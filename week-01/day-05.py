# Modules & Libraries
# Modules are re-useable code files/modules

# random isn't a built in function - you need to import it.
# import random

# from module import functions/variables
# from module import *
# This is to import an individual random module.
# from random import random, randrange, randint


# list = [10, 20, 30]

# # Some built in modules/functions
# list.pop()
# len()
# print()

# # We need to import random, from the Python Standard Library


# random_range = random.randrange(1, 10)
# print(random_range)  # a random number from the specified range.
# x = random.random()  # a floating point number from 0 to 0.99
# print(x)

# # a random integer from the specified range.
# random_int = random.randint(1, 10)
# print(random_int)

# # Random range use case.
# randomEvenNumbers = []
# for i in range(10):
#     randomEvenNumbers.append(random.randrange(0, 200, 2))

# print(randomEvenNumbers)

# -------------------------FUNCTIONS------------------------------

# Subroutines and Functions

# Subroutines

"""
def indentifier():
  code
  code
  code
  code
"""


# def greeting():
#     print("Hello")
#     print("Something else")
#     for i in range(10):
#         print("greeting")


# # Subroutines/Function Invocation
# greeting()


# # function

# print("Hello - built in print function")  # a built in function


# # Parameterised Sub-routines
# def greetings(name, number):
#     print(f"Hello {name}")
#     print("Will print once!")
#     for i in range(number):
#         print(f"Hello {name}")


# greetings("Jonny", 10)


# function syntax: - should have the return keyword

"""
def function_name():
    do something here
    do something else here
    should have the return keyword
"""


def my_function():
    return "return Hello world "


print(my_function())  # just calling a function inside a print()
stored_value = my_function()  # my_function has hello world stored.
print(stored_value)


def squared_number(number):
    # result = number * number
    # return result
    # or
    return (number * number)


print(squared_number(2))
y = squared_number(3)
print(y)


def cubed_number(number):
    return number ** 3


cubed = cubed_number(10)
print(cubed)
