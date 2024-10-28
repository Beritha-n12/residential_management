from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from .models import Building, Room, ResidentProfile, Administrator, RoomApplication, MaintenanceRequest, Event, Communication
from .serializers import BuildingSerializer, RoomSerializer, ResidentProfileSerializer, AdministratorSerializer, RoomApplicationSerializer, MaintenanceRequestSerializer, EventSerializer, CommunicationSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Building
from .serializers import BuildingSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def list(self, request, *args, **kwargs):
        buildings = self.queryset
        serializer = self.get_serializer(buildings, many=True)
        return Response({
            "message": "Buildings retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Building created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building)
        return Response({
            "message": "Building retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Building updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        building = self.get_object()
        serializer = self.get_serializer(building, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Building partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        building = self.get_object()
        self.perform_destroy(building)
        return Response({
            "message": "Building deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        rooms = self.queryset
        serializer = self.get_serializer(rooms, many=True)
        return Response({
            "message": "Rooms retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Room created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room)
        return Response({
            "message": "Room retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Room updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Room partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        room = self.get_object()
        self.perform_destroy(room)
        return Response({
            "message": "Room deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class ResidentProfileViewSet(viewsets.ModelViewSet):
    queryset = ResidentProfile.objects.all()
    serializer_class = ResidentProfileSerializer

    def list(self, request, *args, **kwargs):
        profiles = self.queryset
        serializer = self.get_serializer(profiles, many=True)
        return Response({
            "message": "Resident profiles retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Resident profile created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        return Response({
            "message": "Resident profile retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Resident profile updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Resident profile partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        profile = self.get_object()
        self.perform_destroy(profile)
        return Response({
            "message": "Resident profile deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

    def list(self, request, *args, **kwargs):
        admins = self.queryset
        serializer = self.get_serializer(admins, many=True)
        return Response({
            "message": "Administrators retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Administrator created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        admin = self.get_object()
        serializer = self.get_serializer(admin)
        return Response({
            "message": "Administrator retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        admin = self.get_object()
        serializer = self.get_serializer(admin, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Administrator updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        admin = self.get_object()
        serializer = self.get_serializer(admin, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Administrator partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        admin = self.get_object()
        self.perform_destroy(admin)
        return Response({
            "message": "Administrator deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class RoomApplicationViewSet(viewsets.ModelViewSet):
    queryset = RoomApplication.objects.all()
    serializer_class = RoomApplicationSerializer

    def list(self, request, *args, **kwargs):
        applications = self.queryset
        serializer = self.get_serializer(applications, many=True)
        return Response({
            "message": "Room applications retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Room application created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        application = self.get_object()
        serializer = self.get_serializer(application)
        return Response({
            "message": "Room application retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        application = self.get_object()
        serializer = self.get_serializer(application, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Room application updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        application = self.get_object()
        serializer = self.get_serializer(application, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Room application partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        application = self.get_object()
        self.perform_destroy(application)
        return Response({
            "message": "Room application deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

    def list(self, request, *args, **kwargs):
        requests = self.queryset
        serializer = self.get_serializer(requests, many=True)
        return Response({
            "message": "Maintenance requests retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Maintenance request created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        request_instance = self.get_object()
        serializer = self.get_serializer(request_instance)
        return Response({
            "message": "Maintenance request retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        request_instance = self.get_object()
        serializer = self.get_serializer(request_instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Maintenance request updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        request_instance = self.get_object()
        serializer = self.get_serializer(request_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Maintenance request partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        request_instance = self.get_object()
        self.perform_destroy(request_instance)
        return Response({
            "message": "Maintenance request deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        events = self.queryset
        serializer = self.get_serializer(events, many=True)
        return Response({
            "message": "Events retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Event created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)
        return Response({
            "message": "Event retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Event updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Event partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        event = self.get_object()
        self.perform_destroy(event)
        return Response({
            "message": "Event deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

    def list(self, request, *args, **kwargs):
        communications = self.queryset
        serializer = self.get_serializer(communications, many=True)
        return Response({
            "message": "Communications retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Communication created successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication)
        return Response({
            "message": "Communication retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Communication updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        communication = self.get_object()
        serializer = self.get_serializer(communication, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Communication partially updated successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        communication = self.get_object()
        self.perform_destroy(communication)
        return Response({
            "message": "Communication deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
