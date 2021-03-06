from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_number = models.IntegerField(blank=True)
    location = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.user.username
