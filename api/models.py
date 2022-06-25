from operator import truediv
from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    date_time_stamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.username