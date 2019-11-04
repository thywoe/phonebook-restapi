from django.shortcuts import render
from django.http import JsonResponse

def index(request):
  return JsonResponse(dict(message='Welcome to the Phonebook API'), status=200)
