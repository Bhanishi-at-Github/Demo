'''
    Views for the home app

'''
import hashlib
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .email import verify_email, welcome_email, password_reset
from .serializer import UserSerializer
from .models import User
from cert_project import settings
from .encrypt import encrypt, decrypt

def index(request):
    '''
        Function to render the index page
    '''

    return render(request, 'content/index.html')

def forget_password(request):
    '''
        Function to render the forget password page
    '''

    if request.method == 'POST':

        email = request.POST.get('email')
        print(email)
        password_reset(email)
        messages.success(request, "Email sent successfully!")
        return redirect('/reset_password')

    return render(request, 'clients/forget_password.html')

def logoutuser(request):
    '''
        Function to logout the user
    '''
    try:

        logout(request)
        messages.success(request, "You have successfully logged out.")

        return redirect('/')

    except KeyError as e:

        print(e)
        messages.error(request, "You are not logged in")
        return redirect('login')

def delete(request):

    '''
        Function to delete the user
    '''

    try:

        user = User.objects.get(username=request.user)
        print(user)
        user.delete()
        print("User deleted")
        messages.success(request, "User deleted successfully!")
        print("REDIRECTING")
        return redirect('/')

    except user.DoesNotExist as e:

        print(e)
        messages.error(request, "User does not exist")
        return redirect('/delete_account')

class RegisterAPI(APIView):

    '''
        Function to register the user and send the mail to the user
    '''

    model = User
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/register.html'

    def get(self, request):
        '''
            Function to render the registration page
        '''
        form = UserSerializer()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
            Registering the User model in the admin panel
        '''

        # Getting the data from the request

        if request.method == 'POST':

            first_name = request.data['first_name']
            last_name = request.data['last_name']
            username = request.data['username']
            email = request.POST.get('email')
            password = request.data['password']
            date_of_birth = request.data['date_of_birth']

        # Checking if the email already exists
        if User.objects.filter(email=email).exists():

            print("Email already exists")
            messages.error(request, "Email already exists")
            return redirect('/register')

        rid = random.randint(100000, 999999)
        print("OTP: ", rid)
        verify_email(email, rid)

        # Encrypting the email
        email = encrypt(email, settings.FIELD_ENCRYPTION_KEY)

        print("User Encrypted Email: ", email)

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            rid=rid,
        )

        print("Saved as User: ", email)
        user.set_password(password)
        user.save()

        try:

            if user is not None:

                print("Sending the email")
                print(email)
                print("Email sent!")

            return redirect('/verify')

        except user.DoesNotExist as e:

            print(e)
            messages.error(request, "Email not sent")
            return redirect('/register')


class VerifyAPI(APIView):

    '''
        Function to verify the user
    '''
    model = User
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/verify.html'

    def get(self, request):
        '''
            Function to render the verify page
        '''

        return render(request, self.template_name)

    def post(self, request):
        '''
            Function to verify the user
        '''

        if request.method == 'POST':

            email = request.POST.get('email')
            otp = request.POST.get('otp')

            email = encrypt(email, settings.FIELD_ENCRYPTION_KEY)

            print(email)

            try:

                user = User.objects.get(email=email)

                if user is not None:

                    print("Email found")

                    if user.rid == otp:

                        user.is_verified = True
                        user.save()
                        print(user.is_verified)
                        messages.success(
                            request, 
                            "You have successfully verified."
                        )

                        return redirect('/login')

                    messages.error(request, "Invalid OTP")

                    if user is None:

                        messages.error(request, "Email does not exist")
                        return redirect('/verify')

            except user.is_anonymous as e:

                print(e)
                messages.error(request, "Something went wrong!")
                return redirect('/verify')

        return redirect('/verify')


class LoginAPI(APIView):

    '''
        Function to login the user
    '''
    model = User
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/login_page.html'

    def get(self, request):
        '''
            Function to render the login page
        '''
        return render(request, self.template_name)

    def post(self, request):
        '''
            Function to login the user
        '''

        print("form is valid")

        if request.method == 'POST':

            email = request.POST.get('email')
            print("Email: ", email)

            password = request.POST.get('password')
            print("Password saved")

            welcome_email(email)
            print("Email sent")

            show_email = email
            print("Email: ", show_email)

            email = encrypt(email, settings.FIELD_ENCRYPTION_KEY)

            print("Email: ", email)

            try:

                print("Trying to login")
                user = User.objects.get(email=email)

            except user.DoesNotExist as e:

                print(e)
                user = None
                messages.error(request, "Email does not exist")
                return redirect('/login')

            if user is not None:

                print("Email fetched!")

                if user.check_password(password):

                    print("Checking password")

                    if user.is_verified is True:

                        print("User is verified")

                        login(request, user,
                              backend='django.contrib.auth.backends.ModelBackend')

                        print("Logged in successfully")

                        print("Email: ", show_email)

                        messages.success(request, "Login Successful!")
                        return redirect('/')

                    messages.error(request, "Not verified")
                messages.error(request, "Invalid password")
            
            messages.error(request, "Email does not exist")

        return redirect('/login')


class DeleteUserAPI(APIView):

    '''
        Class to delete the user
    '''

    model = User
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/delete_user.html'

    def get(self, request):
        '''
            Function to render the delete user page
        '''
        return render(request, self.template_name)


class PasswordResetAPI(APIView):

    '''
        Class to reset the password
    '''

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/password_reset.html'
    model = User

    def get(self, request):
        '''
            Function to render the password reset page
        '''
        return render(request, self.template_name)

    def post(self, request):
        '''
            Function to reset the password
        '''

        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            email = encrypt(email, settings.FIELD_ENCRYPTION_KEY)
            user = User.objects.get(email=email)

            if user is not None:

                user.set_password(password)
                user.save()
                return redirect('/login')

            messages.error(request, "Email does not exist")
            return redirect('/password_reset')

        except user.DoesNotExist as e:

            print(e)
            messages.error(request, "Something went wrong!")
            return redirect('/password_reset')


class ProfileAPI(APIView):

    '''
        Class to render the profile page
    '''

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clients/profile.html'

    def get(self, request):
        '''
            Function to render the profile page
        '''

        return render(request, self.template_name)

    def post(self, request):
        '''
            Function to update the profile
        '''
        
        if request.method == 'POST':

            print ("post request")
        
            user = User.objects.get(username = request.user)

            print (user)

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')

            email = encrypt(email, settings.FIELD_ENCRYPTION_KEY)
            
            print ("Details Fetched")

            # if user wants to update specific field in the profile
            
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            
            print("Saved as User")
            
            user.save()

            user = User.objects.get(email = email)

            user.email = decrypt(user.email, settings.FIELD_ENCRYPTION_KEY)
            
            messages.success(request, "Profile Updates Successfully!")
            return redirect('/profile')
