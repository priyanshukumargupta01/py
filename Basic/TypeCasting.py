num_int = 10     # int
num_float = 2.5  # float 
# Python, convert the int value into a float value before performing the addition operation
result = float(num_int) + num_float 
print(result)        # Output: 12.5
print(type(result))  # Output: <class 'float'>


x = float(10)      # 10.0
y = float("25.4")  # 25.4



num = 45
text = str(num)    # "45"
print("Score is: {}".format(text))  # String concatenation ke liye zaroori



print("{}".format(bool(0)))        # False(beacuse 0 is empty value)
print("{}".format(bool("Hello")))  # True(i this case string is not empty)


# List to Set (Duplicates remove karne ke liye)
my_list = [1, 2, 2, 3, 4, 4]
unique_set = set(my_list)      # {1, 2, 3, 4} 
# Set to List
clean_list = list(unique_set)  # [1, 2, 3, 4] 
# List of Pairs to Dictionary
pairs = [("a", 1), ("b", 2)]
my_dict = dict(pairs)          # {'a': 1, 'b': 2}