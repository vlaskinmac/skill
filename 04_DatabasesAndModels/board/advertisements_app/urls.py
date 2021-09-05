from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('advertisements/', views.advertisements),
    path('advertisements/detail/', views.Advertisements.as_view()),
]
