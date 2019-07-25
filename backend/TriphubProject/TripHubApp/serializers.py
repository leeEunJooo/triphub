from rest_framework import serializers
from .models import RoomInput, myRoom


class RoomInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomInput
        fields = "__all__"


class myRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = myRoom
        fields = "__all__"

