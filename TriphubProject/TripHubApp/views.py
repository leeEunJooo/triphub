from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import RoomInput  # 데이터베이스 틀 임포트
from .models import myRoom  # 데이터베이스 틀 임포트
from django.contrib.auth.decorators import login_required
from Members.models import memberList
import pymysql.cursors

# django + react api 연동
from rest_framework import viewsets
from .serializers import RoomInputSerializer, myRoomSerializer


@login_required
def main(request):
    user_name = request.user.username
    user_name += "님 Halo!"
    return render(request, "main.html", {"user_name": user_name})


def index(request):
    # triphub = TripHub
    return render(request, "index.html")


def createroom(request):  # 입력받은 내용을 데이터베이스에 넣어주는 함수
    room = RoomInput()
    room.roomname = request.GET["roomname"]  # 방이름
    room.date = timezone.datetime.now()  # 날짜
    room.mainmember = request.user.username  # 방장
    room.save()  # 쿼리셋 메소드 중 하나. room에 넣은 내용을 저장해라는 함수 객체.delete()객체에 해당하는 내용을 데이터베이스 내용을 지워라

    # 해당 그룹 방 테이블 생성
    myroom = myRoom()
    myroom.room_id = room.id
    myroom.name = room.mainmember
    myroom.save()

    #memberList에 저장
    qs = memberList.objects.all()
    rows = qs.filter(user_id__icontains=request.user.username)
    for row in rows:
        originalvalue = row.room_id
        originalvalue += ('&' + str(room.id))
        rows.update(room_id = originalvalue)
    # memberList.save()
    # rows.update(room_id += ('&' + room.id))
    
    return redirect('Rooms/invite_member')
    
# def myroom(request):  #입력받은 내용을 화면에 띄워주는 함수.
#     return render(request,'main.html')


def info(request):
    return render(request, "info.html")

@login_required
def main(request):
    user_name = request.user.username
    user_name += '님 Halo!'
    
    qs = memberList.objects.all() #유저 정보 모두 가지고 오기
    for row in qs:
        if row.user_id == request.user.username:
            user_room = row.room_id.split('&');
            #유저 방 개수만큼 방을 만듬 -> 유저 방 이름과 함께 띄워주기
            #유저의 방의 개수 배열 user_room
    room_id = []
    room_date = []
    room_roomname = []
    room_mainmember = []
    room_info = []
    user_room = user_room[1:]
    qs = RoomInput.objects.all() #유저 정보 모두 가지고 오기
    cnt = 0
    
    for i in user_room:
        rows = qs.filter(id__icontains=i)
        for row in rows:
            room_id.append(row.id)
            room_date.append(row.date)
            room_roomname.append(row.roomname)
            room_mainmember.append(row.mainmember)
            # room_info.append(a)
    return render(request,'main.html', {'size':len(room_id), 'room_id' : room_id, 'room_date': room_date, 'room_roomname': room_roomname, 'room_mainmember': room_mainmember})
