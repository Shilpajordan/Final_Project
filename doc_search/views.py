from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment, Patient,TimeSlot
from .forms import LoginForm
from .forms import AppointmentBookingForm
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import timedelta




def home(request):
    return render(request, 'doc_search/index.html')


@login_required
def ov_appoint(request):
    doctors = Doctor.objects.all()
    appointments = []
    # print("doc_id:", type(doc_id))

    doc_sel = request.GET.get('doc_sel')

    # print("doc_sel:", type(doc_sel))

    if doc_sel:
        # if doc_id == doc_sel:
        appointments = Appointment.objects.all()
        appointments = appointments.filter(doctor=doc_sel)

    return render(request, 'doc_search/ov_appoint.html', {"doctors": doctors, "appointments": appointments})


@login_required
def detail_appoint(request, patient_id):
    patients = Patient.objects.get(id=patient_id)
    return render(request, 'doc_search/detail_appoint.html', {"patients": patients})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # doc_id = "1"
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('doc_search:ov_appoint', doc_id=doc_id)
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

                  # Send email confirmation to the patient
            name = form.cleaned_data['patient_firstname']
            email = form.cleaned_data['patient_email']
            subject = "Appointment Confirmation"
            message = "Hello, Your appointment has been confirmed. Here is the appointment details:\n\n" + f"Doctor: {appointment.doctor}\nDate: {appointment.date}"

            if not name or not email or not subject or not message:
                return JsonResponse({'status': 'error', 'message': 'Please fill in all fields.'}, status=400)

            try:
                # Include sender's email in the message body
                message_with_email = f"""
                                <html>
                                    <body>
                                        <p><strong>Sender's Email:</strong> {email}</p>
                                        <p>"Hello, Your appointment has been confirmed"</p>
                                        <p>"Here is the appointment details:\n\n"</p>
                                        <p> f"Doctor: {appointment.doctor}\nDate: {appointment.date}"</p>
                                    </body>
                                </html>
                                """

                # send_mail(
                #     subject=f"New contact from {name}: {subject}",
                #     message=message_with_email,
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=[email],
                #     fail_silently=False,
                # )
                # Create the email
                email_message = EmailMultiAlternatives(
                    subject=subject,
                    body=message_with_email,  # Plain text content
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email],
                )

                # Attach the HTML version
                email_message.attach_alternative(message_with_email, "text/html")
                email_message.send()
                #return JsonResponse({'status': 'success', 'message': 'Thank you! Your message has been sent.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            return render(request, 'doc_search/appointment_confirmation.html', {'appointment': appointment})
    else:
        form = AppointmentBookingForm()
    return render(request, 'doc_search/book_appointment.html', {'my_form': form})



def is_time_slot_available(doctor, date):
    # Check if there are any time slots for the given doctor and date
    return TimeSlot.objects.filter(doctor=doctor, start_time__date=date).exists()


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


# Contact Form view

@csrf_exempt
# Adding this  decorator to exempt the view from CSRF verification.
def contact_view(request):
    '''Retrieving Form data from the request'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        '''checking for empty form fields'''
        if not name or not email or not subject or not message:
            '''Return error if any field left empty'''
            return JsonResponse({'status': 'error', 'message': 'Please fill in all fields.'}, status=400)

        try:
            # Adding sender's email in the message body
            message_with_email = f"Sender's Email: {email}\n\n{message}"
            
            '''sending email with the provided details'''
            send_mail(
                subject=f"New contact from {name}: {subject}",
                message=message_with_email,
                from_email=settings.DEFAULT_FROM_EMAIL, 
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            '''Returning success message after the mail sent successfully'''
            return JsonResponse({'status': 'success', 'message': 'Thank you! Your message has been sent.'})
        except Exception as e:
            '''returning error response in case of an exception'''
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    '''render the index.html template if the request method is not POST'''
    return render(request, 'index.html', {'name'})
