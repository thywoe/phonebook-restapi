from rest_framework import serializers
from .models import Phonebook

class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Phonebook
        fields = ("id",'firstname','lastname','Phonenumber','email','address')