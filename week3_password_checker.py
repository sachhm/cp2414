######################
# week3_password_checker.py
#
# 
######################

import random

def main():
    pass


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