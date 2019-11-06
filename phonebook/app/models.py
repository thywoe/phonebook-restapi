from django.db import models

# Create your models here.

class Phonebook(models.Model):
    firstname = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    Phonenumber = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True,null=True)
    address = models.CharField(max_length=50,null=True)
