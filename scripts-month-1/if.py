user_age_input = input("How old are you?")

if not user_age_input.isdigit():
    print("INVALID_INPUT")
    exit()
# Remember that isdigit is a method for strings, that's why I convert age to int later.

user_age_input = int(user_age_input)
allowed_age = 18

if user_age_input >= allowed_age:
    print("you can get in")
else:
    print("you need to be at least 18 years old")

