from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BuildingViewSet,
    RoomViewSet,
    ResidentProfileViewSet,
    AdministratorViewSet,
    RoomApplicationViewSet,
    MaintenanceRequestViewSet,
    EventViewSet,
    CommunicationViewSet,  # Ensure you have this import if you implement CommunicationViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'residents', ResidentProfileViewSet)
router.register(r'administrators', AdministratorViewSet)
router.register(r'room-applications', RoomApplicationViewSet)
router.register(r'maintenance-requests', MaintenanceRequestViewSet)
router.register(r'events', EventViewSet)
router.register(r'communications', CommunicationViewSet)  # Ensure you have this if you implement it

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
