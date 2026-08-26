
# 1. return vs print
def add_with_print(a, b):
    print("Inside add_with_print:", a + b)

def add_with_return(a, b):
    return a + b

res1 = add_with_print(5, 3)
res2 = add_with_return(5, 3)

print("res1 value:", res1)          # None (print doesn't save value)
print("res2 value:", res2)          # 8 (can be reused in math/logic)
print("Using in math:", res2 * 2)   # 16


# 2. Returning Multiple Values (Tuples Unpacking)
def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

stats = get_stats([10, 20, 30, 40, 50])
print("\nReturned Tuple:", stats)

tot, cnt, avg = get_stats([10, 20, 30, 40, 50])
print(f"Total: {tot}, Count: {cnt}, Average: {avg}")


# 3. Early Exit using return
def check_voting_eligibility(age):
    if age < 0:
        return "Invalid age"
    if age >= 18:
        return "Eligible"
    return "Not Eligible"

print("\nAge Checks:")
print("Age -5 :", check_voting_eligibility(-5))
print("Age 21 :", check_voting_eligibility(21))
print("Age 16 :", check_voting_eligibility(16))


# 4. Local vs Global Scope
app_name = "DataApp"  # Global variable

def show_app():
    version = "1.0.0" # Local variable
    print(f"\nInside function: {app_name} v{version}")

show_app()
# print(version)      # NameError: 'version' is not accessible outside


# 5. Modifying Global Variable using 'global' keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print("\nGlobal counter after calls:", counter)


# 6. Nested Functions & 'nonlocal' Keyword
def outer_tracker():
    score = 10  # Enclosing variable

    def inner_boost():
        nonlocal score
        score += 5
        print("Score inside nested function:", score)

    inner_boost()
    print("Score inside outer function:", score)

print("\nTesting nonlocal:")
outer_tracker()