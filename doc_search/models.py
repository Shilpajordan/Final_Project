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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    location = models.CharField(max_length=50, null=True, blank=True)
    specialization = models.CharField(max_length=50, choices=SPEZ_CHOICES, null=False)
    consultation_hours = models.CharField(max_length=50, null=True, blank=True)
    floor_location = models.CharField(max_length=50, choices=FLOOR_CHOICES, null=False, default="Floor 1")
    room_location = models.CharField(max_length=50, choices=ROOM_CHOICES, null=False, default="Room 1")

    class Meta:
        ordering = ['specialization', 'first_name', 'last_name',]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"


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
        verbose_name = "Business Hour"
        verbose_name_plural = "Business Hours"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ['date',]

class TimeSlot(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        start_time_formatted = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{start_time_formatted}"