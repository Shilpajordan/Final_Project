from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor
from .forms import LoginForm
from .forms import AppointmentBookingForm
from .models import Doctor, Patient, Appointment

def home(request):
    return render(request, 'doc_search/index.html')


@login_required
def ov_appoint(request):
    doctors = Doctor.objects.all()
    return render(request, 'doc_search/ov_appoint.html', {"doctors": doctors})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doc_search:ov_appoint')
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()
    return render(request, 'doc_search/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('doc_search:login')


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST)
        if form.is_valid():
            # check availability of the doctor

            appointment = form.save(commit=False)
            # Extract patient name from the form data
            patient_firstname = form.cleaned_data['patient_firstname']
            patient_lastname = form.cleaned_data['patient_lastname']
            patient_age = form.cleaned_data['patient_age']
            patient_gender = form.cleaned_data['patient_gender']
            patient_email = form.cleaned_data['patient_email']
            
            # Lookup patient by name in the database
            try:
                patient = Patient.objects.get(first_name=patient_firstname,last_name=patient_lastname)
            except Patient.DoesNotExist:
                # Handle case where patient doesn't exist
                # You can create the patient here or display an error message
                # For simplicity, I'll create a new patient with the provided name
                patient = Patient.objects.create(first_name=patient_firstname,last_name=patient_lastname,age=patient_age, gender=patient_gender, email=patient_email)
            appointment.patient_id = patient.pk
            appointment.save()
            return render(request, 'doc_search/appointment_confirmation.html', {'appointment': appointment})

    else:
        form = AppointmentBookingForm()
    return render(request, 'doc_search/book_appointment.html', {'my_form': form})
