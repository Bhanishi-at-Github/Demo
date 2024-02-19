'''
Encrypt and decrypt the values

'''
from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models


class EncryptedEmailField(models.EmailField):

    '''
        Class to encrypt and decrypt the values
    '''

    def encrypt_value(self, value):
        '''
        Function to encrypt the value
        '''
        f = Fernet(settings.FERNET_KEY)
        encrypted_value = f.encrypt(value.encode())
        return encrypted_value.decode()

    def decrypt_value(self, encrypted_value):
        '''
            Function to decrypt the value
        '''

        f = Fernet(settings.FERNET_KEY)
        decrypted_value = f.decrypt(encrypted_value).decode()
        return decrypted_value
