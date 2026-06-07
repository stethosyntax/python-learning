

import sys

sys.stdin = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/2. Basics/Practice/input.txt', 'r')
sys.stdout = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/2. Basics/Practice/output.txt', 'w')

# Exercise: Learning Python Basics
print("\n" + "="*80)
print("Exercise: Learning Python Basics")
print("="*80 + "\n")

# Print your name and age.
print("Exercise: Print Name and Age")
print("-"*80)
name = "Laura"
age = 25

print(f"  Name: {name}")
print(f"  Age: {age} years old")

# Create a calculator (+, -, *, /).
print("\n" + "-"*80)
print("Exercise: Simple Calculator (+,-,*,/)")
print("-"*80)

a = 10
b = 3

print(f"  Numbers: {a}, {b}")
print(f"  Sum: {a + b}")
print(f"  Difference: {a - b}")
print(f"  Product: {a * b}")
print(f"  Quotient: {a / b}")

# Check if a number is even or odd.
print("\n" + "-"*80)
print("Exercise: Check Even or Odd")
print("-"*80)

number = 7
print(f"  Number: {number}")
if number % 2 == 0:
    print(f"  {number} is even")
else:
    print(f"  {number} is odd")

# Print numbers from 1 to 10 using a loop.
print("\n" + "-"*80)
print("Exercise: Print Numbers from 1 to 10")
print("-"*80)

for i in range(1, 11):
    print(f"  {i}")

# Write a function to greet someone.
print("\n" + "-"*80)
print("Exercise: Greet Function")
print("-"*80)
def greet(name):
    """Greet a person by name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        None
    """
    print(f"  Hello, {name}! Welcome to Python programming.")

# Function Call
print("Function: greet('Laura')")
greet("Laura") # Calling the greet function with the argument "Laura"

print("\n" + "="*80)
print("END OF EXERCISE")
print("="*80 + "\n")