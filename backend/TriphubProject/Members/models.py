from django.db import models

# Create your models here.

class memberList(models.Model):
    user_id = models.CharField(max_length = 20)   #유저아이디
    room_id = models.CharField(max_length = 10)    #방이름

    def __str__(self) :
        return self.user_id