# 04_lambda_and_builtins.py

# 1. Lambda functions (quick one-liners without a full def)
square = lambda x: x ** 2
add = lambda a, b: a + b

print(square(6))
print(add(5, 7))


# 2. map() - run a function on every item in a list
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

names = ["suman", "aadil", "priyanshu"]
upper_names = list(map(str.upper, names))
print(upper_names)


# 3. filter() - keep only the items that match a condition
scores = [45, 82, 91, 33, 67, 58]

passed = list(filter(lambda s: s >= 60, scores))
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Passed scores:", passed)
print("Even numbers:", evens)


# 4. enumerate() - get both index and item while looping
skills = ["Python", "SQL", "PowerBI", "Pandas"]

# default starts at 0
for idx, skill in enumerate(skills):
    print(f"{idx}: {skill}")

# start ranking from 1 instead
for rank, skill in enumerate(skills, start=1):
    print(f"Rank {rank} -> {skill}")


# 5. zip() - pair items from multiple lists together
names = ["Suman", "Aadil", "Rohit"]
marks = [88, 92, 79]
cities = ["Delhi", "Mumbai", "Patna"]

# stitch lists side by side
for name, score, city in zip(names, marks, cities):
    print(f"{name} scored {score} from {city}")

# easy trick to make a dict out of two lists
scorecard = dict(zip(names, marks))
print("Dict:", scorecard)


# 6. Unzipping paired data back into separate tuples
pairs = [("A", 1), ("B", 2), ("C", 3)]
letters, numbers = zip(*pairs)
print("Letters:", letters)
print("Numbers:", numbers)