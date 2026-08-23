
# 1. Single Argument: range(stop)
# Default start is 0, default step is 1 (generates 0 to 4)
print("1. range(5):", list(range(5)))

# 2. Two Arguments: range(start, stop)
# Starts at 2 and stops before 7 (generates 2 to 6)
print("2. range(2, 7):", list(range(2, 7)))

# 3. Three Arguments: range(start, stop, step)
# Starts at 1, stops before 10, increments by 2 (generates odd numbers)
print("3. range(1, 10, 2):", list(range(1, 10, 2)))