from django.db import models

class Hospital(models.Model):
    SPECIALITY_CHOICES = [
        ('Gastroenterology', 'Gastroenterology - Diagnosis and treatment of digestive system disorders.'),
        ('Hematology and Oncology', 'Hematology and Oncology - Diagnosis and treatment of blood diseases and cancer.'),
        ('Palliative Medicine and Internal Medicine', 'Palliative Medicine and Internal Medicine - Comprehensive care focusing on relief from symptoms and stress of serious illness.'),
        ('Vascular Surgery', 'Vascular Surgery - Treatment of circulatory disorders of arterial and venous vessels.'),
        ('Ear, Nose and Throat Medicine', 'Ear, Nose and Throat Medicine - Treatment of ENT disorders.'),
        ('Cardiology and Intensive Care Medicine', 'Cardiology and Intensive Care Medicine - Diagnosis and treatment of heart conditions and critical care.'),
    ]

    name = models.CharField(max_length=255)
    address = models.TextField()
    visiting_hours_start = models.TimeField(blank=True, null=True)
    visiting_hours_closing = models.TimeField(blank=True, null=True)
    speciality = models.CharField(max_length=255, choices=SPECIALITY_CHOICES)
    number_of_doctors = models.PositiveIntegerField(blank=True, null=True)
    number_of_beds = models.PositiveIntegerField(blank=True, null=True)
    number_of_nurses = models.PositiveIntegerField(blank=True, null=True)
    numbers_of_the_intensive_care_beds = models.PositiveIntegerField(blank=True, null=True)
    emergency_power = models.BooleanField(blank=True, null=True)
    operating_rooms = models.PositiveIntegerField(blank=True, null=True)
    affiliated_specialist_practice = models.PositiveIntegerField(blank=True, null=True)
    outpatient_clinics_focus = models.BooleanField(blank=True, null=True)
    bus_stops_or_parking_spaces = models.TextField(blank=True)
    canteens = models.BooleanField(blank=True, null=True)
    wireless_Internet_access = models.BooleanField(blank=True, null=True)
    aftercare_provider = models.BooleanField(blank=True, null=True)
    discharge_management = models.BooleanField(blank=True, null=True)



    def __str__(self):
        return self.name