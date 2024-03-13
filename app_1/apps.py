'''
App Configurations

'''

from django.apps import AppConfig


class App1Config(AppConfig):

    '''
    Class to configure the app
    '''

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_1'

    def ready(self):
        import app_1.signals
