"""
Author: RL
Date: 2023-03-13
Review on 2023-03-14

Read the Questions and Answer Them as best as you can.
Feel Free to use Previous Notes from Other Lessons.
"???" Fill in the Gaps.

"""
# https://www.w3schools.com/python/python_strings_methods.asp


# Excercise 1
from random import randint
"Given the myString"
myString = "The quick brown fox jumps over the lazy dog"
# 1. Use Slicing to Return the word "jumps".
# 2. Use Slicing to return the words only "quick" and "fox", Combine them into one string.
# 3. Turn the Combined String into Upper Case.

# 1 # 20 to 25
print(myString[20:25])  # jumps

# 2

word1 = myString[4:9]  # quick
print(word1)
word2 = myString[16:19]  # fox

print(f"{word1} {word2}")  # quick fox

# 3

combined = word1 + " " + word2
print(combined.upper())

# Excercise 2
"Given the List of Strings, Complete the code so that the program will Count the number of times a string in the list Starts with a given Prefix."
# Hint: use the startswith() function

List5 = ["car", "dog", "cat", "tree", "cattle", "bush", "camera"]
prefix = "ca"
count = 0
# Complete the Program

for word in List5:
    if word.startswith(prefix):
        count += 1

print(f"The number of times '{prefix}' occurs in the string is {count}")

# Excercise 3
"Build an input: Let the user Enter their First and Last Name in 1 input, then use split() it into 2 variables, first and last name."
"Then, Display the Name as Initials: John Smith > J. S"

full_name = input("Enter your full name: ")

first_name = full_name.split()[0]
last_name = full_name.split()[1]

f_initial = first_name[0]
l_initial = last_name[1]

print(f"Your initials are {f_initial}.{l_initial}")
# Excercise 4
"Online-Style Username/Pseudonym"
"use the random library and string functions from today to build an username generator"
"""
Import the random library: Use Random.Randint() to generate a Online Username. that combines:
	- firstname
	- the Initial of their lastname
	- a random integer
	- all in Lowercase
	- example: TimS#519
"""
my_int = randint(1000, 9999)
user_id = first_name + l_initial + "#" + str(my_int)

user_id = f"{first_name}{l_initial}#{my_int}"
# first_name
# f_initial
# randint(100, 999)

print(user_id.lower())
