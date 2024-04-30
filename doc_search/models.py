from django.db import models
import datetime


class Patient(models.Model):
    CHOICES = [
        ('headache', 'Headache'),
        ('backpain', 'Backpain'),
        ('kneepain', 'Kneepain'),
        ('fever', 'Fever'),
        ('cough', 'Cough'),
        ('throat ache', 'Throat ache'),
        ('sneezing', 'Sneezing'),
        ('body pain', 'Body pain'),
        ('tooth ache', 'Tooth ache'),
        ]
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=10)
    email = models.EmailField(null=False)
    insurance = models.CharField(max_length=50, null=False)
    complaint = models.CharField(max_length=50, choices=CHOICES, null=False)


class Doctor(models.Model):
    SPEZ_CHOICES = [
        ('GP', 'General Practitioner'),
        ('IM', 'Internal Medicine'),
        ('ORTH', 'Orthopedic'),
        ('CARD', 'Cardiologist'),
        ('DENT', 'Dentist'),
        ('GYN', 'Gynecologist'),
        ('PUL', 'Pulmonologist')
    ]
    FLOOR_CHOICES = [
        ('F1', 'Floor 1'),
        ('F2', 'Floor 2'),
        ('F3', 'Floor 3'),
        ('F4', 'Floor 4')
    ]
    ROOM_CHOICES = [
        ('R1', 'Room 1'),
        ('R2', 'Room 2'),
        ('R3', 'Room 3'),
        ('R4', 'Room 4')
    ]
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    specialization = models.CharField(max_length=50, choices=SPEZ_CHOICES, null=False)
    consultation_hours = models.CharField(max_length=50, null=False)
    floor_location = models.CharField(max_length=50, choices=FLOOR_CHOICES, null=False, default="Floor 1")
    room_location = models.CharField(max_length=50, choices=ROOM_CHOICES, null=False, default="Room 1")
    # start_hour = models.TimeField(default=datetime.time(16, 00))
    # end_hour = models.TimeField(default=datetime.time(16, 00))


class BusinessHours(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    ]
    weekday = models.CharField(max_length=50, choices=DAY_CHOICES, null=False)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    
    class Meta:
        ordering = ['id',]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField()
