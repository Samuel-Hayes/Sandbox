"""Samuel Hayes"""

min_length = 6
password = str(input("Password: "))

while len(password) < min_length:
    print("Password length too short")
    password = str(input("Password: "))

print("*" * len(password))
