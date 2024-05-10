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
    email = models.EmailField(null =False)
    insurance = models.CharField(max_length=50, null =True)
    complaint = models.CharField(max_length=50, choices=CHOICES, null =True)


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
    first_name = models.CharField(max_length=50, null =False)
    last_name = models.CharField(max_length=50, null =False)
    location = models.CharField(max_length=50, null =False)
    specialization = models.CharField(max_length=50, choices=SPEZ_CHOICES, null =False)
    consultation_hours = models.CharField(max_length=50, null =False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient_id = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()


class TimeSlot(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        start_time_formatted = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{start_time_formatted}"

