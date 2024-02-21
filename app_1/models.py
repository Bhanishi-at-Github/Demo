'''
Models are used to define the structure of the database.

'''
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from app_1.manager import UserManager


class User(AbstractUser):

    '''
        Class to define the structure of the user table
    '''

    username = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    email = models.CharField(

        max_length=50,
        unique=True,
        blank=False,
        validators=[validators.validate_email]
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    rid = models.CharField(
        max_length=6,
        unique=True,
        null=True,
        blank=True
    )

    is_verified = models.BooleanField(default=False)

    # Replacing the username field with email field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):

        return str(self.username)

