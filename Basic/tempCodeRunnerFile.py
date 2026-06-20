
# Taking multiple inputs in a single line
numbers = input("Enter three numbers separated by spaces: ")
num1, num2, num3 = map(int, numbers.split())
print(f"The three numbers are: {num1}, {num2}, and {num3}")
