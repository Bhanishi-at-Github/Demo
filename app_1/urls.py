'''
Home URL Configuration

'''

from django.urls import path
from .views import index, forget_password, delete, logoutuser
from .views import RegisterAPI, ProfileAPI, LoginAPI, VerifyAPI
from .views import DeleteUserAPI, PasswordResetAPI


urlpatterns = [

    path('', index, name='index'),

    path('register/', RegisterAPI.as_view(), name='register'),

    path('login/', LoginAPI.as_view(), name='login'),

    path('verify', VerifyAPI.as_view(), name='verify'),

    path('logout/', logoutuser, name='logout'),

    path('delete_account/', DeleteUserAPI.as_view(), name='delete'),

    path('profile/', ProfileAPI.as_view(), name='profile'),

    # path('verify_email/' , update_email , name = 'update_email'),

    path('forget_password/', forget_password, name='forget_password'),

    path('reset_password/', PasswordResetAPI.as_view(), name='reset_password'),

    path('deleteuser/', delete, name='deleteuser')

]
