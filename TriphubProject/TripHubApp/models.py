from django.db import models
from django.contrib.auth.models import User

class RoomInput(models.Model) :
    date = models.DateTimeField('date published')   #날짜
    roomname = models.CharField(max_length = 10)    #방이름
    mainmember = models.CharField(max_length = 10)  #방장
    
    def __str__(self) :
        return self.roomname


class myRoom(models.Model):
    room_id = models.CharField(max_length = 10) #룸id
    name = models.CharField(max_length = 10)    #멤버들 이름

    def __str__(self) :
        return self.name


    
    


    

