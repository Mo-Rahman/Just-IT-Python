# More on collections

import array as arr
my_string = "Hello world"

# Characters
"H"
"e"
"l"
"l"
"o"
# and so on...

print(my_string[0])

for letter in my_string:
    print(letter)

# "In" Keyword
# For-In loop
# for i in range
# for element in collection

print("e" in my_string)  # a boolean result. - True
print("z" in my_string)  # False
print("ello" in my_string)  # True
print("z" not in my_string)  # True

search_quote = "going to the shop"
my_letter = "z"

if my_letter in search_quote:
    print(
        f"The letter '{my_letter}' is inside of the string: '{search_quote}'")
else:
    print(
        f"The letter '{my_letter}' is not inside of the string: '{search_quote}'")

basket = ["apples", "bananas", "melon", "mangoes", "lychees"]
fruit = 'grapes'

if fruit in basket:
    print(f"The fruit {fruit} are in the basket")
else:
    print(f"The fruit {fruit} are not in the basket")

# Lists
# Dynamic data structures

basket = ["apples", "bananas", "melon",
          "mangoes", "lychees", 40, 10, True, "John"]

print(basket)
basket.pop()
basket.remove(True)
print(basket)

# basket.sort() # can't sort a mixed value list

numbers = [10, 20, 30]
print(sum(numbers))

numbers2 = [200, 50, 10, True, True]

numbers2.sort()
print(f"test: {numbers2}")

print(sum(numbers2))

# Arrays - Aren't innate to Python, we have to import them. They can only store 1 type of data type inside of it.

# my_arary = arr.array("i", [10, 20, 30, 40])
my_arary = arr.array("i", [10, 20, 30, 40])
my_float = arr.array("f", [10.0, 20.0, 30.0, 40.0])
my_float = arr.array("s", ["apples", "bananas", "melon",
                           "mangoes", "lychees"])

print(type(my_arary))

my_arary.remove(20)
print(my_arary)
print(my_float)
print(type(my_float))
