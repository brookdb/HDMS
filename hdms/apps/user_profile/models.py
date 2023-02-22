from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

#User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name='Location')
    phone = models.CharField(blank=True, null=True, max_length=20, verbose_name='Phone Number')
    ID_Card = models.ImageField(blank=True, null=True, upload_to='profile/img/')

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ['user']
