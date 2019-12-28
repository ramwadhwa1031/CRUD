from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class City(models.Model):
    title=models.CharField(max_length=50)

    
    def __str__(self):
        return self.title


class State(models.Model):
    title=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

class Job(models.Model):
    title=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)