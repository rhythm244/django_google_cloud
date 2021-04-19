from .models import *
from rest_framework import serializers

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['airforce_rank']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['employee_image']

class EmployeeSerializer(serializers.ModelSerializer):

    rank = RankSerializer()
    picture = PictureSerializer()

    class Meta:
        model = Employee
        fields = '__all__'