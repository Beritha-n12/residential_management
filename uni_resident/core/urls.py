from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BuildingViewSet, RoomViewSet, RoomApplicationViewSet, ResidentProfileViewSet,
    AdministratorViewSet, MaintenanceRequestViewSet, EventViewSet, CommunicationViewSet
)

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'room-applications', RoomApplicationViewSet)
router.register(r'residents', ResidentProfileViewSet)
router.register(r'administrators', AdministratorViewSet)
router.register(r'maintenance-requests', MaintenanceRequestViewSet)
router.register(r'events', EventViewSet)
router.register(r'communications', CommunicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
