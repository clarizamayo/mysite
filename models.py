from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Dog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 