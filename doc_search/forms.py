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
GENDERS = [
    ('','Please select your gender'),
    ('MALE','Male'),
    ('FEMALE','Female')
]
class AppointmentBookingForm(forms.ModelForm):
    specialization = forms.ChoiceField(choices=SPEZ_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Please select a doctor", widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    patient_firstname = forms.CharField(max_length=100) 
    patient_lastname = forms.CharField(max_length=100)  
    patient_age = forms.CharField(max_length=100) 
    patient_gender = forms.ChoiceField(choices=GENDERS, widget=forms.Select(attrs={'class': 'form-control'}))
    patient_email = forms.CharField(max_length=100)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].choices = self.get_time_slot_choices()

        # Set placeholders for each field
        self.fields['specialization'].widget.attrs['placeholder'] = 'Please select a specialization'
        self.fields['doctor'].widget.attrs['placeholder'] = 'Please select a doctor'
        self.fields['date'].widget.attrs['placeholder'] = 'Please select a date'
        self.fields['patient_firstname'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['patient_lastname'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['patient_age'].widget.attrs['placeholder'] = 'Enter age'
        self.fields['patient_gender'].widget.attrs['placeholder'] = 'Enter gender'
        self.fields['patient_email'].widget.attrs['placeholder'] = 'Enter email'


 

    def get_time_slot_choices(self):
        # Format the display value and value for each time slot
        res = [(str(time_slot), str(time_slot)) for time_slot in TimeSlot.objects.all()]
        res.insert(0, ('', 'Please select your appintment date & time'))
        return res
    class Meta:
        model = Appointment
        exclude = ["patient_id"] 
        fields = ['specialization', 'doctor', 'date', 'patient_firstname', 'patient_lastname', 'patient_age', 'patient_gender', 'patient_email']



