# Password Policy Validation Engine

print("PASSWORD POLICY VALIDATION ENGINE")

prohibited = ["password", "admin", "qwerty"]


def validate_password(password):
    errors = []

    # Check minimum length
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    # Check uppercase letter
    if not any(ch.isupper() for ch in password):
        errors.append("Password must contain an uppercase letter.")

    # Check lowercase letter
    if not any(ch.islower() for ch in password):
        errors.append("Password must contain a lowercase letter.")

    # Check digit
    if not any(ch.isdigit() for ch in password):
        errors.append("Password must contain at least one digit.")

    # Check special character
    if not any(not ch.isalnum() for ch in password):
        errors.append("Password must contain a special character.")

    # Check three or more consecutive repeated characters
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            errors.append(
                "Password must not contain the same character "
                "3 or more times consecutively."
            )
            break

    # Check prohibited substrings
    lower_password = password.lower()

    for word in prohibited:
        if word in lower_password:
            errors.append(
                "Password must not contain the prohibited "
                "substring '" + word + "'."
            )

    return errors


# Read sample passwords
n = int(input("Enter number of passwords to check: "))

for i in range(n):
    password = input("\nEnter password " + str(i + 1) + ": ")

    errors = validate_password(password)

    print("\nPassword", i + 1, "Validation Result:")

    if len(errors) == 0:
        print("Status: VALID")
        print("All password policy rules are satisfied.")
    else:
        print("Status: INVALID")
        print("Failed Conditions:")

        for error in errors:
            print("-", error)

print("\nPassword validation completed.")
