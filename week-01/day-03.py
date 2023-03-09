# Day 3 Just IT.

# # How the join works.
# array = ["apple", "pears"]
# x = " ".join(array)
# print(x)

# Collections (lists)

# Dynamic Data Structures
array_one = [20, 50, 100, 60]

array_two = [20, 50, 100, 50,  "Hello", "World", 29.99, True, False]

# print(array_two[6])

# # adding Elements to lists
# # list.append(value) - Will add a new value into the list: at the end

# array_one.append(1000)

# print(array_one)

# Inserting a value into a array/list

# array_two.insert(4, "Chocolate")
# print(array_two)

# Removing Elements from a List

# # pop # removes the index if you specify one or the last element
# array_one.pop()
# print(array_one)
# # remove # accepts a value and removes that value from the list


# L = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

# print(L[2][0])

# # Other functions
# # array_one.count() - Finds the number of occurances in a list

# print(array_two.count(50))

# # list.index() - returns the index of the first occurance of a value:
# print(array_one.index(100))
# print(array_one.index(100, 5)) # the second parameter is the starting index.

# # sort() - sorts a list into order: Sorts it in accending order
# array_one.sort()
# print(array_one)

# # Sort a list in decending order
# array_one.sort(reverse=True)
# print(array_one)

# # split() function/method
# sentence = "The dragon becomes me!"

# words = sentence.split()
# print(words)

# # len() function

# length = len(words)
# print(length)
# print(len(sentence))
# print(len(words[1]))

# # split the word easy into a list using LIST()
# word = "Easy"
# x = list(word)
# print(x)

# # join a list of letters
# array = list("Hello")
# joiner = "".join(array)
# print(joiner)

# # max() - finds the max value
# # min() - finds the min value
# list5 = [20, 50, 75, 100, 125, 150]
# print(list5)
# print(min(list5))
# print(max(list5))

# # Removing the highest value
# list5.remove(max(list5))
# print(list5)

# # sum()
# print(sum(list5))

# Exercises day 3

# Resources:
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.w3schools.com/python/python_ref_functions.asp

# """

# ### Excercise 1
# "Given ListA, Perform the following tasks:"
# # Access and Print Oranges
# # Change Pears to Lychee
# # Remove Banana and Apples from the list
# # Print the list.
ListA = ["Banana", "Apples", "Oranges", "Melon", "Pears"]

print(ListA[2])
ListA[-1] = "Lychee"
print(ListA)
ListA.remove("Banana")
ListA.pop(0)
print(ListA)


# ### Excercise 2
# "Given ListB and ListA, Combine the 2 lists into one list, listC."
# "Fill in the gaps"

ListB = ["Ryan", "Lucy", "Kim", "Xin Zhao", "George", "Jake", "Oliver"]
ListC = ListA + ListB
# or
# ListC = ListA.extend(ListB)
print(ListC)


# ### Excercise 3
# "Create a Program that will Let the User Input a Sentence. Find and print the Following:"
# # The First Word
# # The Third Word
# # The Last Word

# sentence = input("Please type a sentence\n")

# split_sentence = sentence.split()
# print(split_sentence)

# print(split_sentence[0])
# print(split_sentence[2])
# print(split_sentence[-1])

# ### Excercise 4
# "Build a Program that lets the user enter Multiple Numbers into an input, seperated by Spaces."
# # Print the Highest Number
# # Print the Sum Of all the numbers
# # Print all the numbers sorted numerically from high to low (Descending).


# Solution 1 using a for loop

# multiple_numbers = input("Enter integers only like so: 10 20 30\n")

# to_array_string = multiple_numbers.split()
# # test_list = ["10", "20", "30", "40"]
# # print(to_array_string)
# array_list = []
# for item in to_array_string:
#     a = int(item)
#     array_list.append(a)
#     # print(array_list)

# print(max(array_list))
# print(sum(array_list))
# array_list.sort(reverse=True)
# print(array_list)

# # Solution 2 - using list and map

multiple_numbers = input("Enter integers only like so: 10 20 30\n")

to_array = multiple_numbers.split()
# test_list = ["10", "20", "30", "40"]

# str_to_int = map(int, to_array) ## saved as <map object at 0x108eb3fa0>
# str_to_int = list(str_to_int)
# Same as above but more succint below
str_to_int = list(map(int, to_array))

print(max(str_to_int))
print(sum(str_to_int))
str_to_int.sort(reverse=True)
print(str_to_int)


multiple_numbers = input("Enter integers only like so: 10 20 30\n")
to_array = multiple_numbers.split()
str_to_int = list(map(int, to_array))

print(max(str_to_int))
print(sum(str_to_int))
str_to_int.sort(reverse=True)
print(str_to_int)


# multiple_numbers = input("Enter integers only like so: 10 20 30\n")

# to_array_string = multiple_numbers.split()

# array_list = []
# for item in to_array_string:
#     a = int(item)
#     array_list.append(a)


# print(max(array_list))
# print(sum(array_list))
# array_list.sort(reverse=True)
# print(array_list)
