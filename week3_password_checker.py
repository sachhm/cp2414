######################
# week3_password_checker.py
#
# 
######################

import random, string, re, json, hashlib

def main():
    pwd = generate_password()
    print(pwd)
    print(check_user_password(pwd))
    encrypt_and_dump(pwd)


def generate_password(length=24):
    """Generate Passwords"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_user_password(password):
     # Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        return False

    # Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        return False

    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # Check for at least one symbol using regular expression
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        return False

    # Check for minimum length
    if len(password) < 8:
        return False

    # If all conditions are met, return True
    return True

def encrypt_and_dump(password): 

    salt = "nerdz"

    Encryptpassword = password+salt

    hashed = hashlib.md5(Encryptpassword.encode())

    print(hashed.hexdigest())

    with open("passes.json", "w") as write_file:
        json.dump(hashed.hexdigest(), write_file)


main()