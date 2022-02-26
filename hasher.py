import hashlib

def hash_password():
    raw_password = input("Password to convert: ")

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

    print("Your secure password is: ")
    print(password)


    # Prompt the user to convert another
    choice = input("Would you like to hash another password? (y/N)")
    if choice == "y":
        hash_password()
    else:
        exit()


print("Welcome! Improve your password system by encorporating SHA256!")
hash_password()