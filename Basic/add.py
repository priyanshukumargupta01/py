#addition
x = 5
y = 3
z = x + y
print(z)

#subtraction
x = 5
y = 3
z = x - y
print(z)

#multiplication
x = 5
y = 3
z = x * y
print(z)

#division
x = 5
y = 3
z = x / y
print(z)

#modulus
x = 5
y = 3
z = x % y
print(z)

#power
x = 5
y = 3
z = x ** y  
print(z)

#assignment operators
x = 5
x += 3  # equivalent to x = x + 3
print(x)

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