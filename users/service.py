import string
import secrets


def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(12))
    return password
