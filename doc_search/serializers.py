from .models import Patient, Doctor, Appointment, BusinessHours
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'email', 'insurance', 'complaint']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'location', 'specialization', 'consultation_hours']


class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHours
        fields = ['id', 'weekday', 'start_hour', 'end_hour']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time']
