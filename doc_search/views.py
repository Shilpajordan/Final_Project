from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment, Patient,TimeSlot
from .forms import LoginForm
from .forms import AppointmentBookingForm
from datetime import datetime
from django.http import JsonResponse


# display the landing page
def home(request):
    return render(request, 'doc_search/index.html')


# list all booked appointments after login
@login_required
def ov_appoint(request):
    doctors = Doctor.objects.all()
    appointments = []

    # check if a specific doctor got selected
    doc_sel = request.GET.get('doc_sel')
    # filter appointments if a specific doctor got selected
    if doc_sel:
        appointments = Appointment.objects.all()
        appointments = appointments.filter(doctor=doc_sel)

    return render(request, 'doc_search/ov_appoint.html', {"doctors": doctors, "appointments": appointments})


# list patient data of a specific appointment
@login_required
def detail_appoint(request, patient_id):
    # get data of specific patient
    patients = Patient.objects.get(id=patient_id)
    return render(request, 'doc_search/detail_appoint.html', {"patients": patients})


# login for staff members to access appointments and patient data
def user_login(request):
    # check if something is posted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check if data entered is correct
        if form.is_valid():
            # read data entered and clean it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # check if entered data matches with existing user
            user = authenticate(request, username=username, password=password)
            # if user is authenticated login and redirect to appointment overview
            if user is not None:
                login(request, user)
                return redirect('doc_search:ov_appoint')
            else:
                messages.error(request, 'Invalid username or password')

    # display empty login form
    else:
        form = LoginForm()
    return render(request, 'doc_search/login.html', {'form': form})


# logout from restricted area
def user_logout(request):
    logout(request)
    return redirect('doc_search:login')


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
            appointment.date = form.cleaned_data['date']
            appointment.save()
            remove_time_slot(appointment.doctor, datetime.strptime(appointment.date, "%Y-%m-%d %H:%M"))

            doctor = form.cleaned_data['doctor']
            return render(request, 'doc_search/appointment_confirmation.html', {'appointment': appointment})
    else:
        form = AppointmentBookingForm()
    return render(request, 'doc_search/book_appointment.html', {'my_form': form})



def is_time_slot_available(doctor, date):
    # Check if there are any time slots for the given doctor and date
    return TimeSlot.objects.filter(doctor=doctor, start_time__date=date).exists()

from datetime import timedelta
def remove_time_slot(doctor, start_time):
    # Remove the time slot for the given doctor and date
    if is_time_slot_available(doctor, start_time):
        end_time = start_time + timedelta(minutes=30)
        try:
            time_slot = TimeSlot.objects.get(doctor=doctor, start_time=start_time, end_time=end_time)
            time_slot.delete()
        except TimeSlot.DoesNotExist:
            # Handle the case where the time slot doesn't exist
            pass



def get_doctors(request):
    specialization = request.GET.get('specialization')
    doctors = Doctor.objects.filter(specialization=specialization).values('id', 'first_name','last_name')
    # Assuming doctors is your queryset result
    doctors_dict = {}
    for doctor in doctors:
        # Extract values from each doctor dictionary
        doctor_id = doctor['id']
        first_name = doctor['first_name']
        last_name = doctor['last_name']
        
        # Construct a new dictionary entry with doctor id as key and other details as value
        doctors_dict[doctor_id] =  first_name+ " " + last_name

    # Now doctors_dict should contain the data in the format you want

    return JsonResponse(doctors_dict)

def get_timeSlots(request):
    doctor = request.GET.get('doctor')
    timeslot = TimeSlot.objects.filter(doctor=doctor).values('id','start_time','end_time')
    # Assuming doctors is your queryset result
    timeslot_dict = {}
    for doctor in timeslot:
        # Extract values from each doctor dictionary
        doctor_id = doctor['id']
        start_time = doctor['start_time'].strftime('%Y-%m-%d %H:%M')

        # Construct a new dictionary entry with doctor id as key and other details as value
        timeslot_dict[doctor_id] =  str(start_time)
    # Now doctors_dict should contain the data in the format you want
    return JsonResponse(timeslot_dict)