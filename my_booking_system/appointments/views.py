from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import User


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            if request.user.is_authenticated:
                appointment.user = request.user
            else:

                admin_user = User.objects.first()
                if admin_user:
                    appointment.user = admin_user
                else:
                    messages.error(request, "Database mein koi user nahi mila. Pehle Admin banayein.")
                    return redirect('book_appointment')

            appointment.save()
            messages.success(request, "Shabaash! Aapki appointment save ho gayi hai.")
            return redirect('book_appointment')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/booking.html', {'form': form})
