#A set in Python is a collection that stores unique (no duplicates) and unordered elements.

# Empty set
s = set()
print(s)

# Set with values
fruits = {"apple", "banana", "mango", "5"}
print(fruits)
print(type(fruits))
print(len(fruits))


#duplicate value
numbers = {1, 2, 3, 2, 1, 4}
print(numbers)
print(len(numbers))


#method in set
set = {1, 2, 3, 4, 5}
set2 = {14, 15, 16, 17, 18}
set.add(6)  # Adds 6 to the set
print(set)
set.remove(3)  # Removes 3 from the set
print(set)
set.discard(4)  # Removes 4 from the set (no error if not present)
print(set)
set.pop()  # Removes and returns an arbitrary element from the set
print(set)
set.update({7, 8, 9})  # Adds multiple elements to the set
print(set)
set.clear()  # Removes all elements from the set
print(set)
set.copy()  # Creates a shallow copy of the set
print(set)
set.union(set2)  # Returns a new set with elements from both sets
print(set.union(set2))
print(set.intersection(set2))  # Returns a new set with elements common to both sets
print(set.difference(set2))  # Returns a new set with elements in set but not in set2
