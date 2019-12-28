from django.contrib import admin

# Register your models here.
from .models import City,Job,Position,State,Employee

admin.site.register(Employee)
admin.site.register(State)
admin.site.register(Job)
admin.site.register(City)
admin.site.register(Position)