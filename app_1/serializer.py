
'''
    Serializers are used to convert the model instances into JSON format
    so that the frontend can easily understand the data.

'''
from rest_framework import serializers
from .models import User

# pylint: disable=too-few-public-methods
class UserSerializer(serializers.ModelSerializer):

    '''
    Defining the serializer class for the User model.

    '''

    class Meta:

        '''
        Passing the model and the fields to the Meta class.

        '''
        model = User

        fields = ['email', 'password', 'first_name', 'username',
                  'last_name', 'date_of_birth', 'is_verified']


class UserLoginSerializer(serializers.ModelSerializer):

    '''
    Defining the serializer class for the User model.

    '''

    class Meta:

        '''
        Passing the model and the fields to the Meta class.

        '''
        model = User

        fields = ['email', 'password']
