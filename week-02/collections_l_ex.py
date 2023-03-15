"""
Author: RL
Date: 2023-02-20
Time: 30 Minutes
Read the Questions and Answer Them as best as you can.
"""

# Excercise 1
"Given List1, Finish the function so that it takes list as a parameter; It will iterate through the list and return the Total Sum of the list"
"Write your solution as a function and Uncomment the Invocation to run your solution."


# def sumList(list):
#     return sum(list)


# list1 = [2, 20, 10, 30, 20, 40, 51, 32, 20]
# print(sumList(list1))

# # ## Excercise 2
# # "This Program will Let the User Build list and print it."
# # "The program should first ask the user how long they want the list to be, then let them keep on entering values until its full."


# def createUserList():
#     List2 = []
#     listLength = int(input("How long do you want the list to be?"))
#     for i in range(listLength):
#         user_item = input("what would you like to enter. ")
#         List2.append(user_item)
#     return List2  # return a list


# var1 = createUserList()
# print(var1)

# # Excercise 3
# "Given the String vowels: Complete the function so that it checks whether or not each vowel exists in a name and tells (prints to) the user of each check."


# def checkForVowels(name):
#     vowels = "aeiou"
#     for letter in vowels:
#         if letter in vowels:
#             print(f"The vowel {letter} is inside the {name}")
#         else:
#             print(f"the vowel {letter} is not inside this {name}")


# name = "Bob Johnson"
# checkForVowels(name)


# # Excercise 4
# "Given List4 of Strings, Complete the function so that it will Reverse Each Word Within the List"
# "EACH of the words should be reversed. Not the List"
# "The Function should Return a list with rev"


# def revEachWord(list):
#     # string[::-1] will reverse a string
#     reversed_word = []
#     for word in list:
#         reversed_word.append(word[::-1])

#     return reversed_word


# List4 = ["Melon", "Banana", "Apple", "Cherry"]
# print(revEachWord(List4))

# ## Extension
# "Adapt Excercise 4 to reverse a list of words from the user."

# print(revEachWord(creatUserList()))
