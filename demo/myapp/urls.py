from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadingscreen, name='loadingscreen'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('loading/', views.loadingscreen, name='loadingscreen'),
    path('universities/', views.universities, name='universities'),
]