# Import only the specific function
from calculator import add

# Take input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call the imported function
result = add(a, b)

print("Sum =", result)