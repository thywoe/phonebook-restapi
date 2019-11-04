from django.urls import path, include
from phonebook.app import views

urlpatterns = [
    path('', views.index, name='index')
]
