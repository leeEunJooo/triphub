from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from TripHubApp.models import myRoom
from TripHubApp.models import RoomInput
from Members.models import memberList
import pymysql.cursors
# from .models import Room

def history(request):
    current_user = request.user
    return render(request,'history.html', {'username':current_user.username})

def invite_all(request):
    myroom = myRoom()   
    users = User()
    newlist = request.GET.get('friends') 
   #방장 찾기
   #방장이 가진 방 번호 추가하기
    friends = newlist.split('&')
    friends = friends[:len(friends)-1]

    qs = memberList.objects.all() #유저 정보 모두 가지고 오기
    #방장 찾기
    room_manager_roomList = []
    mainmanager_recentRoom = ''
    for row in qs:
        if row.user_id == request.user.username:
            room_manager_roomList = row.room_id.split('&');
            mainmanager_recentRoom = room_manager_roomList[len(room_manager_roomList)-1]

    for row in qs:
        for friend in friends:
            if row.user_id==friend:
                #초대한 사람의 member_list에서 room_id에 mainmanager_recentRoom값이 없으면
                room_id_arr = row.room_id.split('&')
                for i in room_id_arr:
                    if i != mainmanager_recentRoom:
                        originalvalue = row.room_id
                        originalvalue += ('&' + str(mainmanager_recentRoom))
                        row.room_id = originalvalue
                        row.save()
                        myroom.room_id = mainmanager_recentRoom
                        myroom.name = friend
                        myroom.save()
        
        # myroom.id #방정보 -> 그 친구 유저 테이블에 room_id 필드에 넣기

        #그 친구 필드에 지금 방 pk값 넣어주기
        #이 행에 그 친구 이름, 룸 아이디, (도시, 선택 여행지 등등 - 아직 필드 안생성함)
    return render(request,'history.html',{'a':originalvalue})
