from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment, Patient
from .forms import LoginForm


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
    print(patient_id)
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
