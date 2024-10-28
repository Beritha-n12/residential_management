from rest_framework import serializers
from .models import User, ResidentProfile, Administrator, Building, Room, RoomApplication, MaintenanceRequest, Event, Communication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Change '_all_' to '__all__'

class ResidentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentProfile
        fields = '__all__'  # Change '_all_' to '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'  # Change '_all_' to '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'  # Change '_all_' to '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Change '_all_' to '__all__'

class RoomApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomApplication
        fields = '__all__'  # Change '_all_' to '__all__'

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'  # Change '_all_' to '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Change '_all_' to '__all__'

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'  # Change '_all_' to '__all__'
