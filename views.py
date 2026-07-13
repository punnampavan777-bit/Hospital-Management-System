from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            #Creates an unsaved Appointment object from the form data and returns unsaved Appointment instance
            appointment = form.save(commit=False)
            # print(type(appointment ))            
            # appointment.patient = Patient.objects.get(user=request.user)#This ensures the appointment is linked to the correct patient account based on who is logged in.
            patient, created = Patient.objects.get_or_create(user=request.user)
            appointment.patient = patient  #manually set user (appoitment to current logged in patient)
            appointment.save()
            messages.success(request,"You have successfully booked your appoinment.")
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    qs=Doctor.objects.all()
    return render(request, 'appointments/book.html', {'form': form,"qs":qs})

def view_appointments(request):
    patient = Patient.objects.get(user=request.user)#current logged in user(patient) related data will be fetched
    appointments = Appointment.objects.filter(patient=patient)   #filter appoints of current patient 
    return render(request, 'appointments/view.html', {'appointments': appointments})


'''
Explanation: 

appointment = form.save(commit=False):
----------------------------------------------
It  creates an unsaved appointment object from the form data.
commit=False	 tells Django not to write it to the database yet.
It gives you a chance to manually assign or modify fields not included in the form.

patient, created = Patient.objects.get_or_create(user=request.user)
---------------------------------------------------------------------------
It tries to find/get an existing Patient object with given condition: user=request.user.If it exists, it returns that 
object and if it does not exist, it creates a new Patient object with user=request.user.
request.user is the currently logged-in user.

patient, created = ...
------------------------
This line unpacks the result into two variables:
patient: The Patient object that was retrieved or created.
created: A boolean. True if a new object was created and False if an existing object was retrieved.


appointment.patient = patient
----------------------------------
It sets current active patient's object (based on the logged-in user) in Appointment model.
This sets up the relationship in the database between the appointment and the patient. 
'''
