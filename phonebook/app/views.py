from django.shortcuts import render
from django.http import JsonResponse
from .models import Phonebook
from .serializers import PhonebookSerializer
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
  return JsonResponse(dict(message='Welcome to the Phonebook API'), status=200)


@api_view(['GET','POST'])
def phonebook_list(request):
  
  if request.method == 'GET':
    phonebooks = Phonebook.objects.all()
    serializer = PhonebookSerializer(phonebooks, many=True)
    return JsonResponse(serializer.data, status=200,safe=False)
  
  elif request.method == 'POST':
    serializer = PhonebookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors, status=400,safe=False)
  
  

@api_view(['GET','PUT','DELETE'])
def phonebook_details(request,pk):
  try:
    phonebook = Phonebook.objects.get(pk=pk)
  except Phonebook.DoesNotExist:
    return JsonResponse(status=404)
  
  if request.method == 'GET':
    serializer = PhonebookSerializer(phonebook)
    return JsonResponse(serializer.data,safe=False)
  
  elif request.method == 'PUT':
    serializer = PhonebookSerializer(phonebook, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors,status=400)
  
  elif request.method == 'DELETE':
    phonebook.delete()
    return JsonResponse(status=204)