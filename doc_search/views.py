import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient
from .forms import LoginForm


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

from .forms import AppointmentBookingForm
from datetime import datetime

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            #1) check availability of the doctor
            
            #2) Lookup patient by name in the database
            try:
                patient_firstname = form.cleaned_data['patient_firstname']
                patient_lastname = form.cleaned_data['patient_lastname']
                patient = Patient.objects.get(first_name=patient_firstname,last_name=patient_lastname)
            except Patient.DoesNotExist:
                # Handle case where patient doesn't exist
                # You can create the patient here or display an error message
                # For simplicity, I'll create a new patient with the provided name
                # Extract patient name from the form data
                patient_age = form.cleaned_data['patient_age']
                patient_gender = form.cleaned_data['patient_gender']
                patient_email = form.cleaned_data['patient_email']
                patient = Patient.objects.create(first_name=patient_firstname,last_name=patient_lastname,age=patient_age, gender=patient_gender, email=patient_email)
            appointment.patient_id = patient.pk
             # Convert date string to datetime object
            # date_str = '2024/05/01 09:30'  # Example date string
            # appointment.date = datetime.strptime(date_str, '%Y/%m/%d %H:%M')
            date_str =  datetime.strptime(form.cleaned_data['date'], '%Y-%m-%d %H:%M:%S%z')
            appointment.date = date_str  # Adjust the format as needed
            appointment.save()

            doctor = form.cleaned_data['doctor']
            #date = '2024/05/01 09:30' #form.cleaned_data['date'].strftime('%Y-%m-%d %H:%M:%S')
            remove_time_slot(doctor, date_str)
            return render(request, 'doc_search/appointment_confirmation.html', {'appointment': appointment})
    else:
        form = AppointmentBookingForm()
    return render(request, 'doc_search/book_appointment.html', {'my_form': form})

from .models import TimeSlot

def is_time_slot_available(doctor, date):
    # Check if there are any time slots for the given doctor and date
    return TimeSlot.objects.filter(doctor=doctor, start_time__date=date).exists()

from datetime import timedelta
def remove_time_slot(doctor, start_time):
    # Remove the time slot for the given doctor and date
    if is_time_slot_available(doctor, start_time):
        end_time = start_time + timedelta(minutes=30)
        print(start_time)
        print(end_time)
        #TimeSlot.objects.filter(doctor=doctor, start_time__date=start_time,end_time__date=end_time).delete()
        try:
            time_slot = TimeSlot.objects.get(doctor=doctor, start_time=start_time, end_time=end_time)
            time_slot.delete()
        except TimeSlot.DoesNotExist:
            # Handle the case where the time slot doesn't exist
            pass

