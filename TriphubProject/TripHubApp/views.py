from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import RoomInput   #데이터베이스 틀 임포트
from .models import myRoom   #데이터베이스 틀 임포트
from django.contrib.auth.decorators import login_required

def index(request):

    # triphub = TripHub
    return render(request,'index.html' )

def createroom(request):    #입력받은 내용을 데이터베이스에 넣어주는 함수
    room = RoomInput()
    room.roomname = request.GET['roomname'] #방이름
    room.date = timezone.datetime.now()  #날짜
    room.mainmember = request.user.username #방장
    room.save() #쿼리셋 메소드 중 하나. room에 넣은 내용을 저장해라는 함수 객체.delete()객체에 해당하는 내용을 데이터베이스 내용을 지워라

    #해당 그룹 방 테이블 생성
    myroom = myRoom()
    myroom.room_id = room.id
    myroom.name = room.mainmember
    myroom.save()
    return redirect('Rooms/invite_member')
    
# def myroom(request):  #입력받은 내용을 화면에 띄워주는 함수.
#     return render(request,'main.html')

def info(request):
    return render(request,'info.html')

@login_required
def main(request):
    user_name = request.user.username
    user_name += '님 Halo!'
    return render(request,'main.html',{'user_name':user_name})