# This function determines "Life stage"
def generate_profile(age):
    if age in range(13):
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"


print("Hello!")
user_name = input("Enter your full name : ")
birth_year_str = input("Enter your birth year : ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year  # calculate the user's age

# User's request for a hobby
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish : ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

# Create a dictionary for user data
user_stage = generate_profile(current_age)
user_profiles = {
    "name": user_name,
    "age": current_age,
    "stage": user_stage,
    "hobbies": hobbies,
}

# Display user profile
print("------------PROFILE SUMMARY------------")
print(f"Name : {user_profiles['name']}")
print(f"Age : {user_profiles['age']}")
print(f"Life stage : {user_profiles['stage']}")
if user_profiles["hobbies"]:
    print(f"Favorite hobbies ({len(user_profiles['hobbies'])}) :")
    for hobby in user_profiles["hobbies"]:
        print(f"- {hobby}")
else:
    print("You didn't mention any hobbies")
print("---------------------------------------")
