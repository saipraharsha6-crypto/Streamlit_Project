from passlib.context import CryptContext
import re

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


def validate_username(username):
    if len(username) < 3:
        return False, "Username must be at least 3 characters."

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        return False, "Username can contain only letters, numbers, and underscores."

    return True, ""


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        return False, "Enter a valid email address."

    return True, ""


def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    if not re.search(r"[A-Za-z]", password):
        return False, "Password must contain at least one letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    return True, ""