from django.urls import path
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('course_1/', views.course_1, name='course_1'),
    path('course_2/', views.course_2, name='course_2'),
    path('course_3/', views.course_3, name='course_3'),
    path('course_4/', views.course_4, name='course_4'),
]