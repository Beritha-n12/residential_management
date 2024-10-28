from django.contrib.auth.models import User
from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_rooms = models.IntegerField()

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.IntegerField()
    room_type = models.CharField(max_length=50)  # e.g., Single, Double
    occupancy_status = models.BooleanField(default=False)  # True if occupied

class RoomApplication(models.Model):
    resident = models.ForeignKey('users.ResidentProfile', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # e.g., Pending, Accepted, Declined
    date_applied = models.DateTimeField(auto_now_add=True)



class ResidentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)

class MaintenanceRequest(models.Model):
    resident = models.ForeignKey('users.ResidentProfile', on_delete=models.CASCADE)
    issue = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  # e.g., Open, In Progress, Resolved
    priority = models.CharField(max_length=20)  # e.g., Low, Medium, High
    date_requested = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

class Communication(models.Model):
    sender = models.ForeignKey('users.ResidentProfile', related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey('users.ResidentProfile', related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
