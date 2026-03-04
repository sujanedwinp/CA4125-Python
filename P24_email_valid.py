import re

try:
    email = input("Enter email: ")

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email Format")

except Exception as e:
    print("Error:", e)