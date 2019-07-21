from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('invite_member',views.history, name="history"),
    path('invite_all',views.invite_all, name="invite_all"),
]