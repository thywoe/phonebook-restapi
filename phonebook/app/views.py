from django.shortcuts import render
from django.http import JsonResponse
from .models import Phonebook
from .serializers import PhonebookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
  return JsonResponse(dict(message='Welcome to the Phonebook API'), status=200)



class AllViews(APIView):
  def get(self, request):
    phonebooks = Phonebook.objects.all()
    serializer = PhonebookSerializer(phonebooks, many=True)
    return Response(serializer.data, status=200)
  
  def post(self,request):
    serializer = PhonebookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=201)
    return Response(serializer.errors, status=400)
  
  

class DetailsView(APIView):
  def get_objects(self,pk):
    try:
      return Phonebook.objects.get(pk=pk)
    except Phonebook.DoesNotExist:
      return Response({'error':'phonebook not found'},status=status.HTTP_404_NOT_FOUND)
  
  def get(self, request, pk=None):
    phonebook = self.get_objects(pk)
    serializer = PhonebookSerializer(phonebook)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk=None):
    phonebook = self.get_objects(pk)
    serializer = PhonebookSerializer(phonebook, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk=None):
    phonebook = self.get_objects(pk)
    phonebook.delete()
    return Response({'message': 'contact deleted successfully'}, status=204)
  