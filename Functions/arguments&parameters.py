# 02_arguments_and_parameters.py

# 1. Positional Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")
describe_pet("Buddy", "dog")


# 2. Keyword Arguments
describe_pet(pet_name="Milo", animal_type="cat")
describe_pet(animal_type="rabbit", pet_name="Snowy")


# 3. Default Arguments
def greet_user(name, message="Welcome to the team!"):
    print(f"Hello {name}, {message}")

greet_user("Suman")
greet_user("Aadil", "Good luck on the test!")


# 4. *args (Arbitrary Positional Arguments)
def calculate_total_sum(*numbers):
    total = sum(numbers)
    print(f"Numbers: {numbers} | Total Sum: {total}")

calculate_total_sum(10, 20)
calculate_total_sum(5, 15, 25, 35, 50)


# 5. **kwargs (Arbitrary Keyword Arguments)
def save_student_profile(name, **details):
    print(f"\nStudent: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")

save_student_profile("Suman", course="Python", role="Data Analyst", city="Delhi")
save_student_profile("Priyanshu", status="Active", batch=2026)


# 6. Combined Order: Positional -> *args -> Default -> **kwargs
def master_function(req_arg, *args, mode="standard", **kwargs):
    print("\n--- Output ---")
    print("req_arg :", req_arg)
    print("args    :", args)
    print("mode    :", mode)
    print("kwargs  :", kwargs)

master_function("User_01", 10, 20, 30, mode="admin", country="India", verified=True)


# 7. Unpacking (* and **)
nums = [100, 200, 300, 400]
calculate_total_sum(*nums)

pet_data = {"animal_type": "parrot", "pet_name": "Rio"}
describe_pet(**pet_data)