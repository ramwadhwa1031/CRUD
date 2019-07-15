from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    prob_type=models.CharField(max_length=40)
    prob_des=models.TextField()