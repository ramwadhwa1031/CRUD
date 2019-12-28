from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    photo=models.ImageField(upload_to='user/%Y/%m/%d/',blank=True)

    def __str__(Self):
        return 'Profile For user {}'.format(Self.user.username)


