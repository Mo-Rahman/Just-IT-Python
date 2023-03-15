"""
Author: RL
Date: 2023-03-15
Time: 30 Minutes

Read the Questions and Answer Them as best as you can.
"???" Fill in the Gaps.

"""

# # Excercise 1
# "Given the TupleA, use a function to find the occuraces of the number 10"
# TupleA = (10, 20, 30, 40, 20, 30, 10, 10)


# def counter(list, value):
#     return list.count(value)


# print(counter(TupleA, 10))

# # Excercise 2
# "Given the Dictionary: person"
# person = {
#     "firstName": "George",
#     "lastName": "Johnson",
#     "Age": 24,
#     "Bio": "A Laid back person.",
#     1: "Some First data",
#     2: "Some Secondary Data",
#     3: 50000
# }

# Solution
# # a.) Delete the Keys 1, 2, 3.
# del person[1]
# person.pop(2)
# del person[3]

# print(person)
# # b.) Add an Address to the Person
# person["Address"] = "London Road"
# print(person)


# # Excercise 3
# "Given setA, verify that Adam and Amy are inside the set."
# setA = {21, 6.9, -6, "Adam", "Danielle", "Pauline", 200, "Amy", "Third"}

# # Solution
# if "Amy" in setA and "Adam" in setA:
#     print("True")


# Excercise 4
"Access and Print the values from the 2D list"
twoList = [
    [12, 43, 5523],
    [4, 5, 553],
    [7, 8, 9]
]

# Solution
# Acccess 553
twoList[1][2]
# Access 8
twoList[2][1]
# Access 9
twoList[2][2]


# #  Excercise 5
# # "Use List Comprehension to Generate a sequence of the first 10 Cubed Numbers"

# Solution
# list_cubed = [(num ** 3) for num in range(1, 11)]
# print(list_cubed)

# Excercise 6
"Given a List namesA, Use List Comprehension to generate a new list with the Length of Each Word."
namesA = ["Luxanna", "Lucy", "Poppy", "Xin Zhao", "George", "Garen", "Oliver"]

# solution
names_numbered = [len(word) for word in namesA]
print(names_numbered)
