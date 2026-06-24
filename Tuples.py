#tuples is a data structure that is used to store multiple items in a single variable. Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

tuple1 = ("apple", "banana", "cherry")
print(tuple1)  # Output: ('apple', 'banana', 'cherry')
print(type(tuple1))  # Output: <class 'tuple'>

#empty tuple
emptyTuple = ()    
print(emptyTuple)  # Output: ()
print(type(emptyTuple))  # Output: <class 'tuple'>


emptyTuple = (1,) 
emptyTuple = (1) 
emptyTuple = (1.0)    
print(emptyTuple)  # Output: ()
print(type(emptyTuple))  # Output: <class 'tuple'>

#tuple with different data types
tuple2 = (1, "Hello", 3.14, True)
print(tuple2)  # Output: (1, 'Hello', 3.14, True)

#tuple methods
tuple3 = (1, 2, 2, 3, 4, 5)
print(tuple3)  # Output: (1, 2, 2, 3, 4, 5)
print(len(tuple3))  # Output: 6
print(tuple3.index(3))  # Returns the index of the first occurrence of 3
print(tuple3.count(2))  # Returns the number of occurrences of 2 in the tuple