# 01_basic_functions.py - Getting started with Python functions

# 1. Defining a simple function and calling it
# Just a basic greeting function that takes no inputs
def greet():
    print("Hey there! Welcome to learning Python functions.")

greet()  # This actually runs the code inside greet()


# 2. Passing data into a function (Parameters & Arguments)
# Here 'name' is a parameter, and we pass a real name when calling it
def greet_user(name):
    print(f"Hi {name}, hope you're having a good day!")

greet_user("Suman")


# 3. Doing some math inside a function
# You can pass more than one value by separating them with commas
def add_numbers(num1, num2):
    total = num1 + num2
    print(f"Adding {num1} and {num2} gives: {total}")

add_numbers(15, 25)


# 4. Adding documentation (Docstrings)
# Triple quotes right under the function line let you explain what it does
def calculate_area(length, width):
    """Calculates the area of a rectangle given length and width."""
    area = length * width
    print(f"Area of the rectangle: {area}")

calculate_area(10, 5)

# You can even read that docstring in your code using .__doc__
print("Function docstring:", calculate_area.__doc__)


# 5. Calling one function inside another
# This keeps code clean and broken down into smaller pieces
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def show_profile(first_name, last_name, role):
    full_name = get_full_name(first_name, last_name)
    print(f"User: {full_name} | Role: {role}")

show_profile("Suman", "Krishna", "Data Analyst")


# 6. Using 'pass' as a placeholder
# Useful when you want to write the function name now but write the logic later
def coming_soon():
    pass  # Keeps Python from throwing an error on an empty function

coming_soon()