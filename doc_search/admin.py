from django.contrib import admin
from doc_search.models import Patient, Doctor, BusinessHours, Appointment


admin.site.register(Patient)
admin.site.register(Appointment)


@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'start_hour', 'end_hour',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'floor_location', 'room_location',)
    list_display_links = ('first_name', 'last_name',)
    fieldsets = [
        ('Doctors', {
            'fields': ('first_name', 'last_name', 'specialization', 'floor_location', 'room_location',)
        })
    ]
