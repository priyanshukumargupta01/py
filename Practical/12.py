#Write a python program to find factorial of a number using Recursion.  

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input
num = int(input("Enter a number: "))

# Display result
print("Factorial of", num, "is:", factorial(num))