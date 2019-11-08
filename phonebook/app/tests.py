from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from .models import Phonebook
from .serializers import PhonebookSerializer

# Create your tests here.
        
class PhonebookTests(APITestCase):
    def setUp(self):
        Phonebook.objects.create(
            firstname='kunle',
            lastname='fola',
            Phonenumber='0802345673',
            email='fola@gmail.com',
            address='2,fola street'
        )
        
    def test_get_phonebook(self):
        url = reverse('phonebook-list')
        response = self.client.get(url)
        phonebook = Phonebook.objects.all()
        serializer = PhonebookSerializer(phonebook , many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



        
class CreatePhonebook(APITestCase):
    def setUp(self):
        self.phonebook = {
            "firstname": 'olakunle',
            "lastname": 'tunde',
            "Phonenumber": '07034212321',
            "email": "kunle@gmail.com",
            "address": '3,kunle street'
        }
        
        self.missing_lastname = {
            "firstname": 'kunle',
            "lastname": '',
            "Phonenumber": '0703444441',
            "email": "shola@gmail.com",
            "address": '3,kunle street'
        }

    def test_create_phonebook(self):
        url = reverse('phonebook-list')
        response = self.client.post(url, self.phonebook, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_missing_phonebook(self):
        url = reverse('phonebook-list')
        response = self.client.post(url, self.missing_lastname, format='json')
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class GetSingleTest(APITestCase):
    
    def setUp(self):
        self.ricky = Phonebook.objects.create(
            firstname='kunle',
            lastname='fola',
            Phonenumber='0802345673',
            email='fola@gmail.com',
            address='2,fola street'
        )
        
    def test_get_valid_phonebook(self):
        response = self.client.get(reverse("phonebook-details", kwargs={'pk':self.ricky.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['firstname'], 'kunle')


class UpdatePhonebook(APITestCase):
    def setUp(self):
        self.ricky = Phonebook.objects.create(
            firstname='shola',
            lastname='pascal',
            Phonenumber='0802345673',
            email='pascal@gmail.com',
            address='2,fola street'
        )
        
        self.valid_update = {
            "firstname":'teni',
            "lastname":'billionaire',
            "Phonenumber":'0802345673',
            "email":'pascal@gmail.com',
            "address":'2,teni street'
        }
        
        self.invalid_update = {
            "firstname":'',
            "lastname":'billionaire',
            "Phonenumber":'0802345673',
            "email":'pascal@gmail.com',
            "address":'2,teni street'
        }
        
    def test_update(self):
        response = self.client.put(reverse('phonebook-details', kwargs={'pk':self.ricky.pk}), self.valid_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_update(self):
        response = self.client.put(reverse('phonebook-details', kwargs={'pk':self.ricky.pk}), self.invalid_update)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class DeletePhonebook(APITestCase):
    def setUp(self):
        self.ricky = Phonebook.objects.create(
            firstname='shola',
            lastname='pascal',
            Phonenumber='0802345673',
            email='pascal@gmail.com',
            address='2,fola street'
        )
        
    def test_delete(self):
        response = self.client.delete(reverse('phonebook-details', kwargs={'pk':self.ricky.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)