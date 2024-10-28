from django.contrib import admin
from .models import (
    Building,
    Room,
    ResidentProfile,
    Administrator,
    RoomApplication,
    MaintenanceRequest,
    Event,
    Communication,
)

# Registering the Building model
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'total_rooms')
    search_fields = ('name', 'address')
    ordering = ('name',)

admin.site.register(Building, BuildingAdmin)

# Registering the Room model
class RoomAdmin(admin.ModelAdmin):
    list_display = ('building', 'floor', 'room_type', 'occupancy_status')
    list_filter = ('building', 'room_type', 'occupancy_status')
    ordering = ('building', 'floor')

admin.site.register(Room, RoomAdmin)

# Registering the ResidentProfile model
class ResidentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number')
    search_fields = ('user__username', 'phone_number')

admin.site.register(ResidentProfile, ResidentProfileAdmin)

# Registering the Administrator model
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'is_superuser')
    search_fields = ('user__username', 'department')

admin.site.register(Administrator, AdministratorAdmin)

# Registering the RoomApplication model
class RoomApplicationAdmin(admin.ModelAdmin):
    list_display = ('resident', 'room', 'status', 'date_applied')
    list_filter = ('status', 'resident')
    ordering = ('-date_applied',)

admin.site.register(RoomApplication, RoomApplicationAdmin)

# Registering the MaintenanceRequest model
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('resident', 'issue', 'location', 'status', 'priority', 'date_requested')
    list_filter = ('status', 'priority')
    ordering = ('-date_requested',)

admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)

# Registering the Event model
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'capacity')
    list_filter = ('date',)
    ordering = ('date',)

admin.site.register(Event, EventAdmin)

# Registering the Communication model
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')
    list_filter = ('sender', 'recipient')
    ordering = ('-timestamp',)

admin.site.register(Communication, CommunicationAdmin)