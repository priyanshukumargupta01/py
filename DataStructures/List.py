#A list is a collection of items in a particular order. In Python, lists are written with square brackets.

marks = [85, 90, 78, 92, 88]
print(marks)  # Output: [85, 90, 78, 92, 88]
print((type(marks)))
print(marks[0])

students = ["Alice","Delhi",213]
print(students)
students[0] = "Bob"
print(students)


#List slicing
list1 = [10, 20, 30, 40, 50]
print(list1[1:4])  # Output: [20, 30, 40]
print(list1[:3])   # Output: [10, 20, 30]
print(list1[2:])  # Output: [30, 40, 50]


#List methods
marks = [85, 90, 78, 92, 88]
marks.append(95)  # Adds 95 to the end of the list
print(marks)
marks.insert(2, 80)  # Inserts 80 at index 2
print(marks)
marks.remove(78)  # Removes the first occurrence of 78
print(marks)
marks.pop()  # Removes the last element
print(marks)
marks.sort()  # Sorts the list in ascending order
print(marks)
marks.sort(reverse=True)  # Sorts the list in descending order
print(marks)
marks.reverse()  # Reverses the list
print(marks)
marks.copy()  # Creates a shallow copy of the list
print(marks)

#list comprehension
squared_numbers = [x**2 for x in range(1, 6)]   
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]