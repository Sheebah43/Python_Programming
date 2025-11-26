# Check the validity of an e-mail {from user input}

import re

check_mail = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    email = email.strip()
    if not email:
        return False
    if " " in email or ".." in email:
        return False
    return bool(check_mail.match(email))

def main():
    e = input("Enter an email address: ").strip()
    if is_valid_email(e):
        print("Valid email.")
    else:
        print("Not a valid email.")

if __name__ == "__main__":
    main()
