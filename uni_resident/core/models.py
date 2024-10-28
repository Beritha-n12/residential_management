from django.contrib.auth.models import User
from django.db import models

# Define room type, application status, and priority choices
ROOM_TYPES = [
    ('Single', 'Single'),
    ('Double', 'Double'),
    ('Suite', 'Suite'),
]

APPLICATION_STATUS = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
]

PRIORITY_LEVELS = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_rooms = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.address}"

    class Meta:
        verbose_name_plural = "Buildings"
        ordering = ['name']


class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    floor = models.IntegerField()
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    occupancy_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room_type} on Floor {self.floor} in {self.building.name}"

    class Meta:
        ordering = ['building', 'floor']


class ResidentProfile(models.Model):
    user = models.OneToOneField(User, related_name="resident_profile", on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Resident Profiles"


class Administrator(models.Model):
    user = models.OneToOneField(User, related_name="administrator_profile", on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.department}"


class RoomApplication(models.Model):
    resident = models.ForeignKey(ResidentProfile, related_name="applications", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="applications", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default='Pending')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.resident.user.username} for Room {self.room}"

    class Meta:
        ordering = ['-date_applied']


class MaintenanceRequest(models.Model):
    resident = models.ForeignKey(ResidentProfile, related_name="maintenance_requests", on_delete=models.CASCADE)
    issue = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default='Open')
    priority = models.CharField(max_length=20, choices=PRIORITY_LEVELS, default='Medium')
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue} - {self.status} (Priority: {self.priority})"

    class Meta:
        ordering = ['-date_requested']


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']


class Communication(models.Model):
    sender = models.ForeignKey(ResidentProfile, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(ResidentProfile, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.user.username} to {self.recipient.user.username} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
