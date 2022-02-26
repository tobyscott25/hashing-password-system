import hashlib

raw_string = input("The password you want to protect: ")

# Because the Python hashlib library cannot hash unicode encoded strings,
# such as those in utf-8, we need to first convert the string to bytes.
# We can do this using the .encode() and .hexdigest() methods.
hashed_string = hashlib.sha256( raw_string.encode('utf-8') ).hexdigest()

print(hashed_string)