import hashlib

def hash_password():
    raw_password = input("Enter your password-system password: ")

    # Because the Python hashlib library cannot hash unicode encoded strings,
    # such as those in utf-8, we need to first convert the string to bytes.
    # We can do this using the .encode() and .hexdigest() methods.
    hash = hashlib.sha256( raw_password.encode('utf-8') ).hexdigest()
    
    # Convert hash to array of all characters
    array = list(hash)
    # Delete every second character from the array
    del array[::2]
    # Rejoin the array to a string
    password = ''.join(array)

    print("Please use the following as as your new secure password: ")
    print(password)

hash_password()