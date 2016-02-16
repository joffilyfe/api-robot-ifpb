from rest_framework import serializers
from robot.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ('id', 'command',)
