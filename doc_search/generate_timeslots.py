import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Append project root directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Configure Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'med_platform.settings')
django.setup()

# Now you can import your models
from doc_search.models import Doctor, TimeSlot

# Function to generate time slots for a given doctor and date range
def generate_time_slots(doctor, start_datetime, end_datetime, duration):
    current_datetime = start_datetime
    while current_datetime < end_datetime:
        end_time = current_datetime + timedelta(minutes=duration)
        TimeSlot.objects.create(doctor=doctor, start_time=current_datetime, end_time=end_time)
        current_datetime = end_time

# Example usage:
doctor = Doctor.objects.get(pk=1)  # Assuming you have a doctor instance
start_datetime = timezone.now().replace(hour=9, minute=0, second=0, microsecond=0)  # Start time for time slots
end_datetime = start_datetime + timedelta(hours=9)  # End time for time slots
duration = 30  # Duration of each time slot in minutes

#☻doctor = Doctor.objects.get(pk=1)  # Assuming you have a doctor instance
#generate_time_slots(doctor, start_datetime, end_datetime, duration)

doctor = Doctor.objects.get(pk=2) 
generate_time_slots(doctor, start_datetime, end_datetime, duration)

#doctor = Doctor.objects.get(pk=3) 
#generate_time_slots(doctor, start_datetime, end_datetime, duration)