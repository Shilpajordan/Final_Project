from django import forms
from .models import Appointment, Doctor


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AppointmentBookingForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    patient_firstname = forms.CharField(max_length=100)  # Add patient name field
    patient_lastname = forms.CharField(max_length=100)  # Add patient name field
    patient_age = forms.CharField(max_length=100)  # Add patient name field
    patient_gender = forms.CharField(max_length=100)  # Add patient name field
    patient_email = forms.CharField(max_length=100)  # Add patient name field
    #date = forms.DateField(input_formats=['%Y/%m/%d'])  # Specify date input format
    #time = forms.TimeField(input_formats=['%H:%M'])  # Specify time input format
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment
        fields = ['date',  'doctor']  # Assuming 'doctor' and 'patient' fields are set automatically

