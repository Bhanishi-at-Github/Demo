'''
Email.py file: used to send email to the user

'''
import hashlib
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail


def hash_value(value):
    '''
        Function to hash the value
    '''

    return hashlib.sha256(value.encode()).hexdigest()


def verify_email(email, rid):
    '''
    verify_email function: To send the mail to the user 
    after signup.

    '''
    print("Processing to send mail")

    my_subject = 'Humanality Welcomes You!'
    html_content = render_to_string(
        'email/verification_email.html',
        {'otp': rid}
    )

    text_content = strip_tags(html_content)

    print("Content rendered successfully. Sending the mail.")

    print(email)

    message = EmailMultiAlternatives(
        subject=my_subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )

    print("Mailling to: ", email)

    print("Mail created. Sending mail....")
    message.attach_alternative(html_content, "text/html")
    message.send()

    print("Mail sent successfully!")
    print("Sent to: ", email)


def welcome_email(email):
    '''
    welcome_email function: To send the mail to the user 
    after signup.

    '''

    my_subject = 'Welcome to Humanality!'
    html_content = render_to_string('email/welcome.html')
    text_content = strip_tags(html_content)

    message = EmailMultiAlternatives(
        subject=my_subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )

    message.attach_alternative(html_content, "text/html")
    message.send()


def password_reset(email):
    '''
    password_reset function: To send the mail to the user 
    after signup to reset the password using send_mail.

    '''

    my_subject = 'Reset your password'
    link = "http://127.0.0.1:8000/reset_password/{hash_value(email)}"
    message = "Click on the link to reset your password: " + link
    send_mail(
        my_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    print("Mail sent successfully!")
