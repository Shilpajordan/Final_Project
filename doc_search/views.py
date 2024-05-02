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
    appointments = Appointment.objects.all()
    return render(request, 'doc_search/ov_appoint.html', {"doctors": doctors, "appointments": appointments})


# TODO filter patients, add url, create html
@login_required
def detail_appoint(request):
    patients = Patient.objects.all()
    return render(request, 'doc_search/detail_appoint.html', {"patients": patients})


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
