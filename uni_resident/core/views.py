from rest_framework import viewsets
from .models import Building, Room, RoomApplication, ResidentProfile, Administrator, MaintenanceRequest, Event, Communication
from .serializers import (
    BuildingSerializer, RoomSerializer, RoomApplicationSerializer, ResidentProfileSerializer,
    AdministratorSerializer, MaintenanceRequestSerializer, EventSerializer, CommunicationSerializer
)

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomApplicationViewSet(viewsets.ModelViewSet):
    queryset = RoomApplication.objects.all()
    serializer_class = RoomApplicationSerializer

class ResidentProfileViewSet(viewsets.ModelViewSet):
    queryset = ResidentProfile.objects.all()
    serializer_class = ResidentProfileSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
