
import random
# More collections

# list, tuples, dictionary, set

# list = [] # like a javascript array
# tuple = ("values", "values") # immutable
# dictionary = {key: value}
# set = {}

# # list
my_list = [1, 2, 3, 4, 5]

# # Tuples are immutable. Only index and count methods are available.
# my_tuple = ("value0", "value1", "value1")
# my_tuple.index()
# my_tuple.count()
# print(my_tuple[1])

# # Sets
# # Unordered/Unindexed, immutable, unique
# # removes duplicates

# my_set = {"a", "b", True, "Jonny", False, "b", "a", True, 10, 20, 30, 40}

# my_set.add("Hello")
# print(my_set)
# my_set.remove("Jonny")
# print(my_set)
# my_set.pop()
# my_set.pop()
# my_set.pop()
# my_set.pop()
# print(my_set)

# # Access sets?

# # Verify if an item is inside a set.
# print(40 in my_set)

# if 40 in my_set:
#     print("Yes")

# for item in my_set:
#     print(item)

# My Random test of id
# # print(id(my_list))
# print(id(my_set))

# print(id(my_list))

# number = 1

# print(id(number))

# # Dictionary

# my_dictionary = {
#     1: "Jonny",
#     2: "Sonny",
#     3: "Donny"
# }

# character = {
#     "first_name": "Bob",
#     "last_name": "Johnson",
#     "age": 25,
#     "bio": "A straight-forward and effective man"
# }

# print(character)

# # accessing Dictionary Values

# print(character["first_name"])

# test = my_dictionary[1]
# print(test)

# # Update values in a dictionary
# character["age"] = 24

# # adding a new key value pair (if the key doesn't exist it will add it)
# character["gender"] = "male"
# print(character)

# # changing/modifying values
# character.update({"bio": "A simple man"})
# print(character)

# # Removing will remove the key and value
# character.pop("age")
# print(character)
# del character["last_name"]
# print(character)

# # List comprehension

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# # How would I make a list of 1 to 50

# # For loop interation

# nums2 = []

# for num in range(1, 21):
#     nums2.append(num)

# print(nums2)

# # List comprehension to do the above but more succinctly.
# # list = [(expression) (for statement)]
# num3 = [num for num in range(1, 26)]
# print(num3)

# sq_numbers = [(num ** 2) for num in range(1, 11)]

# print(sq_numbers)

# list3 = [("Paper" + str(num)) for num in range(1, 11)]

# print(list3)

# list4 = [("Paper" + str(num)) for num in range(1, 11) if num != 6]
# print(list4)

# Nested list / 2D list - A list with a list.

# Method 1: Define lists then stubstitute into greater list

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

grid = [a, b, c]
# print(grid)

# Method: Next lists as we define them

matrix = [
    # 0 #1 #2
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]

# print(matrix)

# Access elements using square brackets
# Access 6
# print(matrix[1][2])
# Access element 8
# print(matrix[2][1])
# shuffle the outer list


# print(matrix)

# for num in range():
#     print(num)
#     for list in matrix:
#         print(list[num])
# print(random.shuffle(list[num]))

# print(len(matrix))

# shuffle the numbers inside the nested list

matrix = [
    # 0 #1 #2
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]

# random.shuffle(matrix) - un-comment to also shuffle outside list.
# shuffle the numbers inside the nested list
for num in range(len(matrix)):
    random.shuffle(matrix[num])
print(matrix)
