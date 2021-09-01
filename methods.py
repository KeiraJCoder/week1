import random
# All libraries should be imported at the very top of your code
print("Hello World")
# String data types - quotation marks
print(5)
# Integer data types - whole numbers
print(3.6)
# Floating points - numbers with a decimal point
print(True)
# Boolean data type - True or False, must be written with a capital letter
print(len("hello world"))
# Len - counts the characters within a string, it also counts the spaces between words
print("Hello World")
len("Hello World")
print(len("3"))
print("hello"[0])
# Remember that Python is 0 index
print("hello".upper())
# .upper() turns all lowercase characters in a string into upper case characters

# This gives us a random floating point between 0 and 1
print(random.uniform(8, 10))
# This gives us a random floating point between the 2 values we give it
print(random.randint(1, 10))
# This gives us a random integer / whole number between the 2 values we give it

# "UPPER"" 
print("word".upper())
#changes all lower case letters to upper case letters

# "LOWER" 
print("WORD".lower())
#changes all upper case letters to lower case letters

# "CAPITALIZE"
print("keira".capitalize())

#capitalises the first letter of the string
"COUNT" #count function counts the number on a specific value
"FIND" #finds the first occurrence of the specified value.
"REPLACE" #replaces a specified phrase with another specified phrase.
"STRIP" #removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)