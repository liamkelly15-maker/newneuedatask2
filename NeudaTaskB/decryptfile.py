# Neueda Task Python script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press Shift+F10 to execute it.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json as j
from cryptography.fernet import Fernet

def load_key():
    """Loads the key from the current directory named `key.key`"""
    return open("../key.key", "rb").read()

def decrypt(filename, key):
    """Given a filename (str or xml) and key (bytes), it decrypts the file and write it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

#load the key
key = load_key()
#check the key
#print(key)
# file name
file = "../json_to_xml.xml"
# decrypt the file
decrypt(file, key)




