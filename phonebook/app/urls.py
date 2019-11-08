from django.urls import path, include
from phonebook.app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('phonebooks/', views.AllViews.as_view(), name='phonebook-list'),
    path('phonebooks/<int:pk>/', views.DetailsView.as_view(), name='phonebook-details')
    
]
