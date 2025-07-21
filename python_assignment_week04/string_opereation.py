def reverse_string(string):
    return string[::-1]

def capitalize_string(string):
    return string.capitalize()

def lowercase_string(string):
    return string.lower()

def uppercase_string(string):
    return string.upper()

import string_opereation as s
sample = "Hello World"

print("Original: ", sample)
print("Reversed: ", s.reverse_string(sample))
print("Capitalized: ", s.capitalize_string(sample))
print("Lowercase: ", s.lowercase_string(sample))
print("Uppercase: ", s.uppercase_string(sample))

"""
Original:  Hello World
Reversed:  dlroW olleH
Capitalized:  Hello world
Lowercase:  hello world
Uppercase:  HELLO WORLD
"""