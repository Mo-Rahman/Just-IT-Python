# Python day 2 - 07/03/2023
# Fundamental Data Types

my_string = "This is a string"  # String
my_int = 100  # Whole numbers
my_float = 10.10  # Float || Decimal (Point) Number
my_boolean = True  # True or False

# Type() function will verify a particular data types

# print(type(my_boolean))  # <class 'bool'>
# print(type(my_int))  # <class 'int'>
# print(type(my_float))  # <class 'float'>
# print(type(my_string))  # <class 'str'>

# Adding 2 numbers from the user
# a = input("Enter Value\n")
# b = input("Enter Value\n")

# concatenating 2 strings - as the input from a and b is a string.
# print(a + b)

# Converting a string to an integer
# a = int(a)
# b = int(b)

# This will add two integer numbers
# print(a + b)

# Arithmetic Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)

# Floor divison (//)
# Modulus (%) - Remainder of a divison
# Exponential (**) - Will raise to the power X * X * X == x ** 3 (X^3)

# Assignment Operator

# Assignment (=) Sets the value

# x = 10  # basic assignment
# print(x)

# x = x + 10
# print(x)
# # Same as above but more succint
# x += x
# print(x)

# # More Data Types (Data structures)
# # list (Same as an array)
# # Tuples

# # A collection of values
# my_list = [300, 400, 10, 80, 20]
# print(type(my_list))
# # Tuples are Immutable
# my_tuple = (200, 400, 40, 650)
# print(type(my_tuple))

# print(my_list)
# print(my_tuple)

# # Accessing a list

# print(my_list[2])

# # Updating values

# my_list[1] = 450

# print(my_list)


# Strings

# name = "Jonny"

# print(name)


# Escape Character
# They start with back-slash \n
# \\n to escape the \
# \t - Will make an indentation (tab)
# \\ - will let you type a \

# sentence = "Were going to write out a sentence here.\\n\nHere is another sentence on a new line in the terminal."

# print(sentence)
# # Multi-line Strings

# sentence_two = """ It means I can type some sentences out.
# This is what they use to create ascii art
#    ----
#      ----  YNWA  ------
#      'What will this look like'
# """

# print(sentence_two)

# # String Formatting

# fruit1 = "apples"
# fruit2 = "strawberries"
# fruit3 = 'banana'

# print(f"Today I ate some {fruit1}, {fruit2} and {fruit3}")


# Excercise 1
# "Build a program that will Let the user Input 2 numbers the Users."
# "The Program should print the Sum, Difference, Multiplication and Division of the numbers."

input_one = int(input("Input one\n"))
input_two = int(input("Input two\n"))

print(f"The sum of two numbers {input_one + input_two}\nMultiplication {input_one * input_two}\nThe division: {input_one / input_two} the modulus of input one {input_one % 4} the modulus of input one {input_two % 4} ")

# Excercise 2
"Let the user Input 2 numbers and Build a program that finds an area of triangle"
# 1/2 Base x Height

base = int(input("Enter base\n"))
height = int(input("Enter height\n"))

print(f"{(base / 2) * height}")


# Excercise 3
"Kilometers to Miles Converter"
"Build a Program that will let the user input a Distance in Kilometers and Convert it to miles"
# Conversion factor: 1 mile = 1.6km

distance_in_km = float(input("Enter distance in KM\n"))

print({distance_in_km / 1.6})

# Excercise 4
"Temperature Unit Converter (Celcius to Fahernheit)"
"Build a program that will let the user Input a Temperature in Celcius and Print a the value converted into Fahernheit."
# Formula for °C to °F: F = (celcius * (9/5)) + 32

celcius_to_fahernheit = float(input("Enter Celcius\n"))

print(f"{(celcius_to_fahernheit * (9/5)) + 32}")
