from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from .models import Appointment, Doctor, TimeSlot
SPEZ_CHOICES = [
    ('', 'Please select a specialization'),  # Default option
    ('GP', 'General Practitioner'),
    ('IM', 'Internal Medicine'),
    ('ORTH', 'Orthopedic'),
    ('CARD', 'Cardiologist'),
    ('DENT', 'Dentist'),
    ('GYN', 'Gynecologist'),
    ('PUL', 'Pulmonologist')
]
class AppointmentBookingForm(forms.ModelForm):
    specialization = forms.ChoiceField(choices=SPEZ_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    date = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    patient_firstname = forms.CharField(max_length=100)  # Add patient name field
    patient_lastname = forms.CharField(max_length=100)  # Add patient name field
    patient_age = forms.CharField(max_length=100)  # Add patient name field
    patient_gender = forms.CharField(max_length=100)  # Add patient name field
    patient_email = forms.CharField(max_length=100)  # Add patient name field
    #date = forms.DateField(input_formats=['%Y/%m/%d'])  # Specify date input format
    #time = forms.TimeField(input_formats=['%H:%M'])  # Specify time input format
    #date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    #date = forms.ModelChoiceField(queryset=TimeSlot.objects.all())
    # Customize the display and value of the time slot choices
    
    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].choices = self.get_time_slot_choices()

    def get_time_slot_choices(self):
        # Format the display value and value for each time slot
        return [(str(time_slot.start_time), str(time_slot)) for time_slot in TimeSlot.objects.all()]
    class Meta:
        model = Appointment
        exclude = ["patient_id"]  # Assuming 'doctor' and 'patient' fields are set automatically
        fields = ['specialization', 'doctor', 'date', 'patient_firstname', 'patient_lastname', 'patient_age', 'patient_gender', 'patient_email']



