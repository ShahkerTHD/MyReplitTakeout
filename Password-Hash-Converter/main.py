# the password of the user

import hashlib

password = input("Enter your password: ")

hash_object = hashlib.sha256(password.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
