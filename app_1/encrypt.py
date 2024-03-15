'''
    Encrypt and decrypt the data using AES encryption algorithm
'''

import hashlib
from Crypto.Cipher import AES

def pad(data):

    '''
    Add padding to the data to make it multiple of 16
    '''
    # Create padding length
    length = 16 - (len(data) % 16)
    # Adding padding length to the data
    data += bytes([length]) * length
    return data

def encrypt(plain_text, key):

    '''
    Encrypt the data using AES encryption algorithm
    '''

    iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    enc_digest = hashlib.md5(key.encode('utf-8'))
    enc_cipher = AES.new(enc_digest.digest(), AES.MODE_CBC, iv)
    # Converting the data into byte code
    plain_text = pad(plain_text.encode('utf-8'))
    # Converting the data into hexadecimal
    encrypted_text = enc_cipher.encrypt(plain_text).hex()
    return encrypted_text

def unpad(text):

    '''
    Get the last byte, which indicates the padding length
    '''

    padding_length = text[-1]
    # Remove the padding bytes
    return text[:-padding_length]

def decrypt(cipher_text, key):

    '''
    Decrypt the data using AES encryption algorithm
    '''

    iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    dec_digest = hashlib.md5(key.encode('utf-8'))
    dec_cipher = AES.new(dec_digest.digest(), AES.MODE_CBC, iv)
    encrypted_text = bytes.fromhex(cipher_text)
    # Decrypt the data
    decrypted_text = dec_cipher.decrypt(encrypted_text)
    # Converting the data into plain text
    result_text = unpad(decrypted_text).decode('utf-8')
    return result_text
