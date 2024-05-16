from django.contrib import admin
from doc_search.models import Patient, Doctor, BusinessHours, Appointment, TimeSlot


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(TimeSlot)
@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('weekday', 'start_hour', 'end_hour')

# from django.contrib import admin
# from doc_search.models import Patient, Doctor, BusinessHours, Appointment


# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'age', 'gender', 'email', 'insurance', 'complaint',)


# @admin.register(BusinessHours)
# class BusinessHoursAdmin(admin.ModelAdmin):
#     list_display = ('weekday', 'start_hour', 'end_hour',)


# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'specialization', 'floor_location', 'room_location',)
#     list_display_links = ('first_name', 'last_name',)
#     fieldsets = [
#         ('Doctors', {
#             'fields': ('first_name', 'last_name', 'specialization', 'floor_location', 'room_location',)
#         })
#     ]


# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('patient', 'doctor', 'date',)
