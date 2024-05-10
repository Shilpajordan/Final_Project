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
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Please select a doctor")
    date = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    patient_firstname = forms.CharField(max_length=100) 
    patient_lastname = forms.CharField(max_length=100)  
    patient_age = forms.CharField(max_length=100) 
    patient_gender = forms.CharField(max_length=100) 
    patient_email = forms.CharField(max_length=100)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].choices = self.get_time_slot_choices()
 

    def get_time_slot_choices(self):
        # Format the display value and value for each time slot
        res = [(str(time_slot), str(time_slot)) for time_slot in TimeSlot.objects.all()]
        res.insert(0, ('', 'Please select your appintment date & time'))
        return res
    class Meta:
        model = Appointment
        exclude = ["patient_id"] 
        fields = ['specialization', 'doctor', 'date', 'patient_firstname', 'patient_lastname', 'patient_age', 'patient_gender', 'patient_email']



