from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('<int:payment_id>/', views.payment_detail, name='payment_detail'),
]
