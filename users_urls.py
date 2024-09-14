from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_list, name='user_list'),
]
