from django.db import models

# Create your models here.

class BroadcastNotification(models.Model):
    
    '''
        Class to define the structure of the notification table
    '''
    message = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    sent = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['-date']