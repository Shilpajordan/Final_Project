from django.contrib import admin
from doc_search.models import Patient, Doctor,  Appointment, TimeSlot


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(TimeSlot)
