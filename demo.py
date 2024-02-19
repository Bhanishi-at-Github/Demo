import hashlib


def hash_value(value):
    '''
        Function to hash the value
    '''

    return hashlib.sha256(value.encode()).hexdigest()

