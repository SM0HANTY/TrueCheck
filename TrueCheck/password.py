import numpy as np

# For student login with an auto-generated password
def auto_student_password(password_length):
    characters_available = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")  # All possible characters
    return ''.join(np.random.choice(characters_available, password_length))

auto_generated_password = auto_student_password(8)
print(f"Auto-generated password: {auto_generated_password}")

# For self-password setup
def self_student_password(user_password_input):
    fixed_password_length = 9
    input_length = len(user_password_input)

    if input_length > fixed_password_length:
        print(f"Password length should be within {fixed_password_length} characters.")
        return  # Exits the function without proceeding further

    # Initialize variables
    accept_input = []
    upper_case_check = 0
    lower_case_check = 0
    digit_check = 0

    # Check each character
    for char in user_password_input:
        if char.isupper():
            upper_case_check = 1
            accept_input.append(char)
        elif char.islower():
            lower_case_check = 1
            accept_input.append(char)
        elif char.isdigit():
            digit_check = 1
            accept_input.append(char)

    # Validation checks
    if upper_case_check and lower_case_check and digit_check:
        if len(accept_input) <= fixed_password_length:
            print(f"Password {''.join(accept_input)} is valid and set.")
        else:
            print(f"Password length exceeds the fixed limit of {fixed_password_length} characters.")
    else:
        print("Password must include at least one uppercase letter, one lowercase letter, and one number.")

# Example usage
user_input = input("Enter your desired alphanumeric password: ")
self_student_password(user_input)
