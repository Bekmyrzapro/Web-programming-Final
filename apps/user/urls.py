from allauth.account import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("signup/", views.signup, name="custom_signup"),
]