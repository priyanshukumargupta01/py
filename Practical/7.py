# Write a program to demonstrate working with dictionaries in python.   


student = {
    "Name": "Priyanshu",
    "Age": 21,
    "Course": "B.Tech CSE",
    "City": "Jalandhar"
}

# Display dictionary
print("Student Dictionary:", student)

# Accessing values
print("Name:", student["Name"])
print("Course:", student["Course"])

# Adding a new item
student["College"] = "CT Group of Institutions"
print("After Adding College:", student)

# Updating a value
student["Age"] = 22
print("After Updating Age:", student)

# Removing an item
student.pop("City")
print("After Removing City:", student)

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())