from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.Select(),
            'end_time': forms.Select(),
        }

    start_time = forms.DateTimeField(widget=forms.Select(choices=[]))
    end_time = forms.DateTimeField(widget=forms.Select(choices=[]))

