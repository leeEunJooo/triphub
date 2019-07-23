from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from TripHubApp.models import myRoom
from TripHubApp.models import RoomInput
import pymysql.cursors
# from .models import Room

def history(request):
    current_user = request.user
    return render(request,'history.html', {'username':current_user.username})

def invite_all(request):
    myroom = myRoom()
    users = User()
    newlist = request.GET.get('friends')
   
    friends = newlist.split('&')
    for obj in users.objects.all().filter(classname__contains=username):
        for i in range(0, len(friends)-1):
            
    # for i in range(0,len(friends)):
    #     # queryset = queryset[:1]
    #     # queryset.
    #     myroom.name = friends[i]

    # myroom.save()
    # myroom = myRoom()
    return render(request,'history.html',{'name':friends})
