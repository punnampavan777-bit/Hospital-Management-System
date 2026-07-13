from django import forms
from .models import Appointment
# from doctors.models import Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'age', 'contact', 'decease', 'doctor']
