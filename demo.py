import hashlib
from cryptography.fernet import Fernet
from cert_project import settings

def hash_value(value):
    '''
        Function to hash the value
    '''

    return hashlib.sha256(value.encode()).hexdigest()

def decrypt_value(hash_value):
    '''
        Function to decrypt the value
    '''

    f = Fernet(settings.FERNET_KEY)
    decrypted_value = f.decrypt(hash_value).decode()
    return decrypted_value


val = "Hello"
encrypt = hash_value(val)

print("Encrypted : ", encrypt)

print ("Decrypted: ", decrypt_value(encrypt))