import hashlib

def hash_password():
    raw_string = input("Enter your password-system password: ")

    # Because the Python hashlib library cannot hash unicode encoded strings,
    # such as those in utf-8, we need to first convert the string to bytes.
    # We can do this using the .encode() and .hexdigest() methods.
    hashed_string = hashlib.sha256( raw_string.encode('utf-8') ).hexdigest()

    print("Please use the following as as your new secure password: ")
    print(hashed_string)

hash_password()