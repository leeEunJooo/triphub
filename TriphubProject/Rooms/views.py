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
    friends = friends[:len(friends)-1]

    qs = User.objects.all() #유저 정보 모두 가지고 오기
    
    isvalid = []
    room = '' 
    for name in friends:
        validname = qs.filter(username__icontains=name)
        # myroom.id #방정보 -> 그 친구 유저 테이블에 room_id 필드에 넣기

        #그 친구 필드에 지금 방 pk값 넣어주기
        #이 행에 그 친구 이름, 룸 아이디, (도시, 선택 여행지 등등 - 아직 필드 안생성함)
        

    # friends = friedns[:10]
    # for obj in users.objects.all().filter(classname__contains=username):
    #     for i in range(0, lenfriends)-1):
            # (
    # for i in range(0,len(friends)):
    #     # queryset = queryset[:1]
    #     # queryset.
    #     myroom.name = friends[i]

    # myroom.save()
    # myroom = myRoom()
    return render(request,'history.html',{'name':validname})
