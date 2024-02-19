# Generated by Django 5.0.1 on 2024-02-12 05:34

import django.core.validators
import encrypted_model_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=encrypted_model_fields.fields.EncryptedCharField(unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]