from django.db import models


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
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    specialization = models.CharField(max_length=50, choices=SPEZ_CHOICES, null=False)
    consultation_hours = models.CharField(max_length=50, null=False)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField()
