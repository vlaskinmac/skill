from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('advertisements/<int:pk>/', views.AdvertisementsDetailView.as_view()),
    path('advertisements/', views.AdvertisementsListView.as_view()),
]
