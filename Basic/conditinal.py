# Conditional Statements in Python

x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")





x = 15
y = 15  

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")


#if-else statement
age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


#if-elif-else Statement   
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Under Age")


#traffic light example
light = input("enter the light color of traffic light(red, yellow, green):")    
if light == "red":
    print("stop")
elif light == "yellow":
    print("ready to go") 
elif light == "green":
    print("go")       
else:
    print("enter a valid color")    


 #Ternary Operator
age = 20
print("You can vote") if age >= 18 else print("You cannot vote")   