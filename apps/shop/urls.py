from django.contrib import admin
from django.urls import path, include

from apps.shop.views import MainView, CreateOrderView

urlpatterns = [
    path('', MainView.as_view()),
    path('order/<int:pk>', CreateOrderView.as_view(), name='order')
]