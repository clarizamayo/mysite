from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Dog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 

class Adoption(models.Model):
    email = models.EmailField(max_length=50, unique=False)
    message = models.TextField()