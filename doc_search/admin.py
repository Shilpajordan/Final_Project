from django.contrib import admin
from doc_search.models import Patient, Doctor, BusinessHours, Appointment


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)

@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'start_hour', 'end_hour',)
