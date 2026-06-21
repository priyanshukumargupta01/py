print("23")
print("23" + "23" == "2323")

name = "John"
age = 30
print("Hello, " + name + "! You are " + str(age) + " years old.")


print(type(name))
print(type(age))
print(type(3.14))
x = 10
y = 3.14
print(type(x))
print(type(y))

#string
greeting = "Hello, World!"
print(greeting)
#integer
age = 30
print(age)
#float
pi = 3.14
print(pi)
#boolean
is_student = True
print(is_student)
# List
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Tuple
coordinates = (10, 20)
print(coordinates)
# Dictionary
person = {"name": "John", "age": 30}
print(person)

a = 10
b = "Priyanshu"
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


A,B = 3,2
C=4.0
txt = "Priyanshu "
print(A*B*txt)
print(A*(B*txt))  #CONCATENATION
print(A+B*C)
print((A+B)*C)

greeting = "Hello, World!"
print(greeting[0])  # H 
print(greeting[1])  # W
print(greeting[-1]) # !
print(greeting[0:5]) # Hello
print(greeting[7:])  # World!
print(greeting[:5])  # Hello
print(greeting[::2]) # Hlo ol!
print(greeting[::-1]) # !dlroW ,olleH
print(greeting.upper()) # HELLO, WORLD!
print(greeting.lower()) # hello, world!
print(greeting.replace("World", "Python")) # Hello, Python!
print(greeting.split(", ")) # ['Hello', 'World!']
print(greeting.strip("!")) # Hello, World
print(greeting.find("World")) # 7
print(greeting.count("o")) # 2