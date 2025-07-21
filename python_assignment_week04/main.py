import string_opereation as s
import calculator as c
import lambda_calculator as lc

print("Using calculator.py:")
print("Addition:", c.add(10, 5))
print("Subtraction:", c.subtract(10, 5))
print("Multiplication:", c.multiply(10, 5))
print("Division:", c.divide(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", s.reverse_string(sample_string))
print("Capitalized:", s.capitalize_string(sample_string))
print("Lowercase:", s.lowercase_string(sample_string))
print("Uppercase:", s.uppercase_string(sample_string))

"""
Expected output:
Using calculator.py:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

Using string_operations.py:
Original: hello World
Reversed: dlroW olleh
Capitalized: Hello world
Lowercase: hello world
Uppercase: HELLO WORLD
"""