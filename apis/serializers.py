from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'visiting_hours_start', 'visiting_hours_closing', 'speciality', 'number_of_doctors', 'number_of_doctors', 'number_of_beds', 'number_of_nurses', 'numbers_of_the_intensive_care_beds', 'emergency_power', 'operating_rooms', 'affiliated_specialist_practice', 'outpatient_clinics_focus', 'bus_stops_or_parking_spaces', 'canteens', 'wireless_Internet_access', 'aftercare_provider', 'discharge_management']
