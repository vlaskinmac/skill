from django.urls import path
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('course_1/', views.course_1, name='advertisement/course_1.html'),
    path('course_2/', views.course_1, name='advertisement/course_2.html'),
    path('course_3/', views.course_1, name='advertisement/course_3.html'),
    path('course_4/', views.course_1, name='advertisement/course_4.html'),
]