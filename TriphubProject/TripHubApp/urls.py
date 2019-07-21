# TripHubApp urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('main',views.main, name="main"),
    path('createroom',views.createroom, name="createroom"),
    # 패스를 추가해줬다고 무조건 html을 띄워야 하는 건 아님.
    # path('어떤 url이 들어오면', (어디에있는)어떤 함수를 실행시켜라)
    # 그저 create 함수를 실행시켜주려고 하는 것임.
]