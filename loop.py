# Loop Examples

#for loop
for i in range(5):
    print(i)        

#while loop
count = 0
while count < 5:
    print(count)
    count += 1

#nested loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  

#Using continue
for i in range(5):
    if i == 2:
        continue
    print(i) 



#range() function
#### The range() function generates an immutable sequence of numbers within a specified interval, commonly used for controlling loop iterations   ###.

# 1. Single Argument: range(stop)
# Default start is 0, default step is 1 (generates 0 to 4)
print("1. range(5):", list(range(5)))

# 2. Two Arguments: range(start, stop)
# Starts at 2 and stops before 7 (generates 2 to 6)
print("2. range(2, 7):", list(range(2, 7)))

# 3. Three Arguments: range(start, stop, step)
# Starts at 1, stops before 10, increments by 2 (generates odd numbers)
print("3. range(1, 10, 2):", list(range(1, 10, 2)))

# 4. Reverse / Decrement: Negative Step
# Starts at 10 and steps backward down to 1 (countdown)
print("4. range(10, 0, -1):", list(range(10, 0, -1)))

# 5. Negative numbers with range
# Starts at -5, increments by 2, stops before 5
print("5. range(-5, 5, 2):", list(range(-5, 5, 2)))

print("-" * 45)

#Practical Loop & Indexing Examples

# Standard loop execution
print("6. Loop execution:")
for i in range(1, 4):
    print("   Iteration number:", i)

# Iterating through list indices using range() and len()
fruits = ["apple", "banana", "cherry"]
print("7. Iterating with len():")
for index in range(len(fruits)):
    print("   Index {}: {}".format(index, fruits[index]))