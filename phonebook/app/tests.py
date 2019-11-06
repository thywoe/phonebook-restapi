from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Phonebook

# Create your tests here.

class PhonebookTests(APITestCase):
    def test_create_phonebook(self):
        url = reverse('phonebook-list')
        data = {
            "firstname": 'Kunle',
            "lastname": 'tunde',
            "Phonenumber": '07034212321',
            "email": "kunle@gmail.com",
            "address": '3,kunle street'
        }

        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_phonebook(self):
        url = reverse('phonebook-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_one(self):
        url = reverse('phonebook=details')
        response = self.client