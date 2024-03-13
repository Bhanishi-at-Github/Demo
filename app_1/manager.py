
'''
Custom User Model : a custom user model to add some extra fields to the user model. 

'''

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    '''
        UserManager : to create a user and a superuser.

    '''

    use_in_migrations = True

    def create_user(self, email=None, password=None, **extra_fields):
        '''
        create_user function: To create a user.
        '''

        if not email:
            raise ValueError('The email address must be provided.')

        first_name = extra_fields.pop('first_name', None)
        last_name = extra_fields.pop('last_name', None)
        rid = extra_fields.pop('rid', None)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            rid=rid,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Defining the functions to create a superuser

    def create_superuser(self, email, password, **extra_fields):
        '''
        create_user function: To create a user.

        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Super user validations

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to True.')

        return self.create_user(email, password, **extra_fields)
