from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
import calendar

def appointment_add(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

        now = datetime.now()
        end_date = now + timedelta(days=30)
        available_slots = []
        while now <= end_date:
            if now.weekday() < 5:  # Mo-Fri
                for hour in range(8, 19):
                    for minute in [0, 30]:
                        slot_time = datetime(now.year, now.month, now.day, hour, minute)
                        available_slots.append((slot_time, slot_time.strftime('%Y-%m-%d %H:%M')))
            now += timedelta(days=1)

        form.fields['start_time'].widget.choices = available_slots
        form.fields['end_time'].widget.choices = available_slots
        
    return render(request, 'appointment_add.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})



