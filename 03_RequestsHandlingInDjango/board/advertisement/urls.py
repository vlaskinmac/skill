from django.urls import path
from .import views

urlpatterns = [
    path('contacts/', views.Contacts.as_view()),
    path('advertisement/', views.CBV.as_view()),
    path('about/', views.Companies.as_view()),
    path('', views.AdvertisementList.as_view()),
]