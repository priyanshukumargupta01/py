# Input and Output in Python

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying the input
print(f"Hello, {name}! You are {age} years old.")

#float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

# Taking multiple inputs in a single line
numbers = input("Enter three numbers separated by spaces: ")
num1, num2, num3 = map(int, numbers.split())
print(f"The three numbers are: {num1}, {num2}, and {num3}")
