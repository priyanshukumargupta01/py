######### arithmetic operators

a = 15
b = 4 
print("Given Values -> a = {}, b = {}\n".format(a, b)) 
# 1. Addition (+)
addition = a + b
print("Addition (a + b))          : {}".format(addition))
# 2. Subtraction (-)
subtraction = a - b
print("Subtraction (a - b)         : {}".format(subtraction))

# 3. Multiplication (*)
multiplication = a * b
print("Multiplication (a * b)      : {}".format(multiplication))

# 4. Float Division (/) -> Always returns float
division = a / b
print("Float Division (a / b)      : {}".format(division))

# 5. Floor Division (//) -> Returns integer quotient (rounds down)
floor_division = a // b
print("Floor Division (a // b)     : {}".format(floor_division))

# 6. Modulus (%) -> Returns remainder
modulus = a % b
print("Modulus/Remainder (a % b)   : {}".format(modulus))

# 7. Exponentiation (**) -> Power (a^b)
power = a ** b
print("Exponentiation (a ** b)     : {}".format(power))

print("-" * 45) 
# String Concatenation & Replication
str1 = "Data"
str2 = "Analyst"
print("String Concatenation (+)    : {}".format(str1 + ' ' + str2))
print("String Replication (*)      : {}".format('Python! ' * 3)) 
# Precedence Example (PEMDAS: (), **, *, /, +, -)
complex_exp = 10 + 2 * (3 ** 2) / 2
print("Operator Precedence Result  : {}".format(complex_exp))



####Relational Operators

a = 20
b = 10

print("Given Values -> a = {}, b = {}\n".format(a, b))
# 1. Equal to (==)
print("Is a equal to b? (a == b)                 : {}".format(a == b))
# 2. Not Equal to (!=)
print("Is a NOT equal to b? (a != b)             : {}".format(a != b))
# 3. Greater than (>)
print("Is a greater than b? (a > b)              : {}".format(a > b))
# 4. Less than (<)
print("Is a less than b? (a < b)                 : {}".format(a < b))
# 5. Greater than or equal to (>=)
print("Is a greater than or equal to 20? (a >= 20): {}".format(a >= 20))
# 6. Less than or equal to (<=)
print("Is b less than or equal to 5? (b <= 5)     : {}".format(b <= 5))

print("-" * 50)
 
# Chained Comparison (Python allows chaining)
age = 22
print("Is age between 18 and 30? (18 <= age <= 30) : {}".format(18 <= age <= 30))
# String Comparison (ASCII/Lexicographical order)
# 'apple' comes before 'banana', so 'apple' < 'banana' is True
print("String comparison ('apple' < 'banana')     : {}".format('apple' < 'banana'))