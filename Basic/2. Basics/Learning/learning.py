"""Python Basics Learning Module.

This module demonstrates fundamental Python concepts including:
- Variables and data types (int, float, str, bool)
- String operations (concatenation, slicing, methods)
- Arithmetic and logical operators
- Conditional statements (if/elif/else)
- Loops (for, while)
- Functions

The script reads from input.txt and writes output to output.txt.
"""

import sys

sys.stdin = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/2. Basics/Learning/input.txt', 'r')
sys.stdout = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/2. Basics/Learning/output.txt', 'w')

# ============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# ============================================================================

print("\n" + "="*80)
print("1. VARIABLES AND DATA TYPES")
print("="*80 + "\n")

name = "Laura"
print(f"  {name} is a girl")
print(f"  {name} is also known as good at learning")
print(f"  {name} is doing her best to learn python")
print(f"  {name} is a good learner")

print("\n" + "-"*80)
print("1.1 Variable Descriptions:")
print("-"*80)

age = 25
height = 5.6
is_student = True

print(f"  Name: {name}")
print(f"  Age: {age} years old")
print(f"  Height: {height} feet tall")
print(f"  Is Student: {is_student}")

# ============================================================================
# SECTION 2: STRING OPERATIONS
# ============================================================================

print("\n" + "="*80)
print("2. STRING OPERATIONS")
print("="*80 + "\n")

# String Definition Methods
print("2.1 String Definition Methods:")
print("-"*80)
name = "Laura"
print(f"  Single quotes: '{name}'")
print(f"  Double quotes: \"{name}\"")
print(f"  Triple quotes: \"\"\"{name}\"\"\"")

detail = "It's a nice day"
description = 'She said "Hello"'
print(f"  With apostrophe: {detail}")
print(f"  With quotes: {description}")

# String Concatenation
print("\n" + "-"*80)
print("2.2 String Concatenation:")
print("-"*80)
first_name = "Laura"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"  First Name: {first_name}")
print(f"  Last Name: {last_name}")
print(f"  Full Name: {full_name}")
print(f"  Greeting: Hello {full_name}")

# String Repetition
print("\n" + "-"*80)
print("2.3 String Repetition:")
print("-"*80)
repeated = first_name * 3
print(f"  '{first_name}' × 3 = {repeated}")

# String Length
print("\n" + "-"*80)
print("2.4 String Length:")
print("-"*80)
print(f"  Length of '{first_name}': {len(first_name)} characters")

# String Indexing and Slicing
# Note: Indexing starts at 0, negative indexing starts at -1 from the end
# Slicing syntax: string[start:end] (end is exclusive)
# Strings are immutable, so slicing creates a new string rather than modifying the original
print("\n" + "-"*80)
print("2.5 String Indexing and Slicing:")
print("-"*80)
print(f"  String: {first_name}")
print(f"  Index [0] (first char): {first_name[0]}") # Accesses the first character 'L'
print(f"  Index [-1] (last char): {first_name[-1]}") # Accesses the last character 'a'
print(f"  Slice [1:4]: {first_name[1:4]}") # Slices from index 1 to index 4 (exclusive)
print(f"  Slice [:3]: {first_name[:3]}") # Slices from the start to index 3 (exclusive)
print(f"  Slice [2:]: {first_name[2:]}") # Slices from index 2 to the end

# Escape Characters
print("\n" + "-"*80)
print("2.6 Escape Characters:")
print("-"*80)
print("  Newline example:")
print("    Line 1\n    Line 2") # \n creates a new line
print("  Tab example:")
print("    Name:\tLaura") # \t creates a tab space
print("  Quote example:")
print('    She said "Hello"') # Using single quotes to include double quotes without escaping
print("    It\'s a nice day") # Using backslash to escape the apostrophe

# String Formatting
print("\n" + "-"*80)
print("2.7 String Formatting:")
print("-"*80)
age = 25
print(f"  Using f-string: {name} is {age} years old") # f-strings allow embedding expressions inside string literals
print("  Using .format(): {} is {} years old".format(name, age)) # .format() method replaces {} with the provided arguments 

# String Methods
# Note: String methods return new strings and do not modify the original string since strings are immutable
print("\n" + "-"*80)
print("2.8 String Methods:")
print("-"*80)
text = "  HeLlo World  "
print(f"  Original text: '{text}'")
print(f"  .title():    '{text.title()}'") # Converts the first character of each word to uppercase and the rest to lowercase
text = text.capitalize() # Converts the first character to uppercase and the rest to lowercase
print(f"  .upper():    '{text.upper()}'")
print(f"  .lower():    '{text.lower()}'")
print(f"  .strip():    '{text.strip()}'")
print(f"  .replace('World', 'Python'): '{text.replace('World', 'Python')}'")
print(f"  .find('World'): {text.find('World')}")

# ============================================================================
# SECTION 3: ARITHMETIC OPERATORS
# ============================================================================

print("\n" + "="*80)
print("3. ARITHMETIC OPERATORS")
print("="*80 + "\n")

print("Given: a = 10, b = 3\n")
a, b = 10, 3

print(f"  Addition (a + b):       {a} + {b} = {a + b}")
print(f"  Subtraction (a - b):    {a} - {b} = {a - b}")
print(f"  Multiplication (a * b): {a} * {b} = {a * b}")
print(f"  Division (a / b):       {a} / {b} = {a / b}")
print(f"  Floor Division (a // b):{a} // {b} = {a // b}")
print(f"  Modulus (a % b):        {a} % {b} = {a % b}")
print(f"  Power (2 ** 3):         2 ** 3 = {2 ** 3}")

# ============================================================================
# SECTION 4: TYPE CONVERSION
# ============================================================================

print("\n" + "="*80)
print("4. TYPE CONVERSION")
print("="*80 + "\n")

print("String to Integer:")
age = "25"
age_num = int(age)
print(f"  age = '{age}' (str) → int(age) = {age_num} (int)")

print("\nFloat to String:")
price = 99.99
price_str = str(price)
print(f"  price = {price} (float) → str(price) = '{price_str}' (str)")

print("\nInteger to Float:")
count = 10
count_float = float(count)
print(f"  count = {count} (int) → float(count) = {count_float} (float)")

# ============================================================================
# SECTION 5: COMPARISON OPERATORS
# ============================================================================

print("\n" + "="*80)
print("5. COMPARISON OPERATORS")
print("="*80 + "\n")

print("Comparison Results:")
print(f"  5 == 5 (Equal):        {5 == 5}")
print(f"  5 != 3 (Not Equal):    {5 != 3}")
print(f"  5 > 3 (Greater Than):  {5 > 3}")
print(f"  5 < 3 (Less Than):     {5 < 3}")
print(f"  5 >= 5 (Greater or Equal): {5 >= 5}")
print(f"  5 <= 3 (Less or Equal):    {5 <= 3}")

# ============================================================================
# SECTION 6: CONDITIONAL STATEMENTS
# ============================================================================

print("\n" + "="*80)
print("6. CONDITIONAL STATEMENTS")
print("="*80 + "\n")

# Grade Assignment
print("6.1 Grade Assignment based on Marks:")
print("-"*80)
marks = 85
print(f"  Marks: {marks}")
if marks >= 90:
    print(f"  → Grade: A (Excellent)")
elif marks >= 80: # Elif statement to check if marks are between 80 and 89
    print(f"  → Grade: B (Good)")
else:
    print(f"  → Grade: C (Satisfactory)")

# Adult Status
print("\n" + "-"*80)
print("6.2 Age Classification:")
print("-"*80)
age = 20
status = "Adult" if age >= 18 else "Minor" # Ternary operator for concise if-else
print(f"  Age: {age}")
print(f"  → Status: {status}")

# Access Control
print("\n" + "-"*80)
print("6.3 Access Control:")
print("-"*80)
age = 20
has_id = True
print(f"  Age: {age}, Has ID: {has_id}")
if age >= 18 and has_id: # Logical operator 'and' to check multiple conditions
    print(f"  → Access: Can enter")
else:
    print(f"  → Access: Denied")

# Greatest of Three Numbers
print("\n" + "-"*80)
print("6.4 Greatest of Three Numbers:")
print("-"*80)
num1, num2, num3 = 10, 20, 20
print(f"  Numbers: {num1}, {num2}, {num3}")
if num1 > num2 and num1 > num3:
    print(f"  → Greatest: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"  → Greatest: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"  → Greatest: {num3}")
elif num1 == num2 or num1 == num3 or num2 == num3: # Logical operator 'or' to check for duplicates
     print(f"  → Note: There are duplicate greatest numbers")
else:
    print(f"  → Note: All numbers are equal")

# Working Age Range
print("\n" + "-"*80)
print("6.5 Working Age Range:")
print("-"*80)
age = 25
print(f"  Age: {age}")
if 18 <= age <= 65: # Chained comparison for checking if age is between 18 and 65
    print(f"  → Status: Working age")

# Index Out of Range for short-circuit evaluation
# Note: Always check list length before accessing an index to avoid IndexError
# In this example, we check if the list has more than 3 elements before trying to access index 3 (which is the 4th element)
print("\n" + "-"*80)
print("6.6 Index Out of Range Check:")
print("-"*80)
numbers = [10, 20, 30]
if len(numbers) > 3:
    print(numbers[3])
else:
    print("Index is out of range")

# Chain Comparison for name length classification
print("\n" + "-"*80)
print("6.7 Name Length Classification with Chain Comparison:")
print("-"*80)
name = "Laura"
print(f"  Name: {name}")
if len(name) > 1 and (name[1] == 'L' or name[-1] == 'a'):
    print(f"  → Category: Name either second letter with 'L' or ends with 'a'")
else:
    print(f"  → Category: Name does not meet the criteria")

# ============================================================================
# SECTION 7: LOOPS
# ============================================================================

# Note: Loops are used to execute a block of code repeatedly until a certain condition is met.
print("\n" + "="*80)
print("7. LOOPS")
print("="*80 + "\n")

# For Loop with Range (0 to 4)
# Note: The for loop iterates over a sequence (like a list, string, or range). The range() function is commonly used to generate a sequence of numbers for iteration.
# Note: The range() function generates a sequence of numbers. range(start, stop) generates numbers from start to stop-1. If start is omitted, it defaults to 0.
print("7.1 For Loop with Range (0 to 4):")
print("-"*80)
for i in range(0, 5):
    print(f"  Iteration {i}")

# For Loop with Range
print("\n" + "-"*80)
print("7.1.1 For Loop with Range (0 to 4):")
print("-"*80)
for i in range(5):
    print(f"  Iteration {i}")

# For Loop with Step
print("\n" + "-"*80)
print("7.1.2 For Loop with Step (0 to 9 with step of 2):")
print("-"*80)
for i in range(0, 10, 2): # Loop from 0 to 9 with a step of 2 (0, 2, 4, 6, 8)
    print(f"  Iteration {i}")

# Nested For Loop
# Note: A nested loop is a loop inside another loop. The inner loop will complete all its iterations for each iteration of the outer loop.
print("\n" + "-"*80)
print("7.2 Nested For Loop:")
print("-"*80)
for i in range(0, 2):
    print(f"  Iteration of i {i}")
    print(f"  → Starting inner loop for j")
    for j in range(0, 3):
        print(f"    Iteration of j {j}")
    print(f"  → Completed inner loop for i {i}")

# For-Else Loop
# Note: The else block in a for loop executes after the loop finishes iterating over all items, unless the loop is terminated by a break statement. If a break occurs, the else block is skipped.
print("\n" + "-"*80)
print("7.3 For-Else Loop:")
print("-"*80)
for i in range(3):
    print(f"  Iteration {i}")
else:
    print(f"  → Loop completed without break")

# For-else Loop with Break
print("\n" + "-"*80)
print("7.3.1 For-Else Loop with Break:")
print("-"*80)
for i in range(3):
    print(f"  Iteration {i}")
    if i == 1:
        print(f"  → Breaking the loop at iteration {i}")
        break
else:
    print(f"  → Loop completed without break")

# For Loop with List
print("\n" + "-"*80)
print("7.4 For Loop with List:")
print("-"*80)
fruits = ["apple", "banana"]
for idx, fruit in enumerate(fruits, 1):
    print(f"  {idx}. {fruit}")

# While Loop
# Note: A while loop continues to execute as long as the condition is true. It is important to ensure that the loop will eventually terminate by modifying the condition variable within the loop.
print("\n" + "-"*80)
print("7.5 While Loop (count from 0 to 2):")
print("-"*80)
i = 0
while i < 3:
    print(f"  Iteration {i}")
    i += 1
else:
    print(f"  → Loop completed!")

# Infinite Loop (commented out to prevent execution)
# Note: An infinite loop continues to execute indefinitely because the loop condition is always true. It is important to ensure that there is a way to break out of the loop to avoid crashing the program.
# print("\n" + "-"*80)
# print("7.5.1 Infinite Loop (commented out):")
# print("-"*80)
# while True:
#     print("  This is an infinite loop. Press Ctrl+C to stop it.") 

# ============================================================================
# SECTION 8: FUNCTIONS
# ============================================================================

print("\n" + "="*80)
print("8. FUNCTIONS")
print("="*80 + "\n")

# Note: A function is a reusable block of code that performs a specific task. Functions can take parameters (inputs) and return values (outputs). They help to organize code, improve readability, and reduce redundancy.
# Note: The def keyword is used to define a function, followed by the function name and parentheses. The function body is indented below the definition line. The return statement is used to specify the value that the function should return to the caller.
# Note: Functions can be called by using their name followed by parentheses, and passing any required arguments inside the parentheses.
# Note: A non-returnable function does not return a value. It performs an action, such as displaying output, but does not send a result back to the caller.
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
print("-"*80)

# Note: This function takes two parameters (a and b), adds them together, and returns the result. The function can handle both integers and floats due to Python's dynamic typing.
# Note: A returnable function returns a value to the place where it was called using the return statement. The caller can then use this returned value for further processing or display.
def add(a, b):
    """Add two numbers and return the result.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# Function Call
print("Function: add(5, 3)")
result = add(5, 3)
print(f"  Result: {result}")

print("\n" + "="*80)
print("END OF BASICS MODULE")
print("="*80 + "\n")