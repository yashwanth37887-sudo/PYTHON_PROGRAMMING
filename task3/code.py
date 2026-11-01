
import re

# Function to validate student email
def validate_email(email):
    errors = []

    # Check missing components
    if email.count("@") != 1:
        errors.append("Invalid or missing @ separator")
        return errors

    username, domain = email.split("@")

    if not username:
        errors.append("Missing username")

    if not domain:
        errors.append("Missing domain")

    # Check username format
    if username:
        if not re.fullmatch(r"[A-Za-z0-9._-]+", username):
            errors.append("Invalid characters in username")

        if (username.startswith(".") or
                username.endswith(".") or
                ".." in username):
            errors.append("Malformed username separators")

    # Check domain format
    if domain:
        if "." not in domain:
            errors.append("Missing domain extension")
        else:
            parts = domain.split(".")

            if len(parts) != 2 or not all(parts):
                errors.append("Malformed domain separators")
            else:
                name, extension = parts

                if not re.fullmatch(r"[A-Za-z0-9-]+", name):
                    errors.append("Invalid characters in domain")

                if (name.startswith("-") or name.endswith("-")):
                    errors.append("Malformed domain separators")

                if not re.fullmatch(r"[A-Za-z]{2,}", extension):
                    errors.append("Invalid domain extension")

    return errors


# Function to validate registration ID
def validate_registration(reg_id):
    errors = []

    pattern = r"STU-[0-9]{4}-[0-9]{4}"

    if not reg_id:
        errors.append("Registration ID is missing")

    elif not re.fullmatch(pattern, reg_id):
        errors.append("Invalid registration ID format")

        parts = reg_id.split("-")

        if len(parts) != 3:
            errors.append("Missing or malformed separators")

        else:
            if parts[0] != "STU":
                errors.append("Invalid prefix")

            if not parts[1]:
                errors.append("Missing year")
            elif not re.fullmatch(r"[0-9]{4}", parts[1]):
                errors.append("Invalid year character group")

            if not parts[2]:
                errors.append("Missing student number")
            elif not re.fullmatch(r"[0-9]{4}", parts[2]):
                errors.append("Invalid student number character group")

    return errors


# Main program
print("STUDENT EMAIL AND IDENTIFIER VALIDATION")
print("---------------------------------------")

email = input("Enter Student Email: ")
reg_id = input("Enter Registration ID: ")

# Email validation
email_errors = validate_email(email)

print("\nEMAIL VALIDATION:")
if email_errors:
    print("Invalid Email")
    for error in email_errors:
        print("-", error)
else:
    print("Valid Email")

# Registration ID validation
id_errors = validate_registration(reg_id)

print("\nREGISTRATION ID VALIDATION:")
if id_errors:
    print("Invalid Registration ID")
    for error in id_errors:
        print("-", error)
else:
    print("Valid Registration ID")

print("\nVALIDATION COMPLETED")
