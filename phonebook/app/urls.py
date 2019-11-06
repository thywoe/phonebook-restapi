from django.urls import path, include
from phonebook.app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('phonebooks/', views.phonebook_list, name='phonebook-list'),
    path('phonebooks/<int:pk>/', views.phonebook_details, name='phonebook-details')
    
]
