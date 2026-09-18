# Write a python program to find largest of three numbers.  

# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Find the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Display result
print("The largest number is:", largest)