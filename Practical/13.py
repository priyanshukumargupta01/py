#Write a program that accepts the lengths of three sides of a triangle as inputs.  The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides).  

# Input three sides of a triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check Pythagorean theorem
if a**2 + b**2 == c**2:
    print("The triangle is a right triangle.")
elif a**2 + c**2 == b**2:
    print("The triangle is a right triangle.")
elif b**2 + c**2 == a**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")