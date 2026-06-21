#logical operators
x = True
y = False
print(x and y)  # False

a=3
b=5
if a > 0 and b > 0:
    print("Both numbers are positive")
elif a > 0 or b < 0:
    print("At least one number is not positive")
elif not a > 0:
    print("a is not positive")
else:
    print("Both numbers are not positive")