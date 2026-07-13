from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) #-
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.IntegerField()
    decease = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)# -Listouts doctors names  in the form
    
    #Optional method

    # def __str__(self):
    #     return f"{self.name} - {self.doctor.name}"




'''
patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

Ans:

This is a one-to-many relationship.
Each Appointment belongs to one Patient and one Patient can have many Appointments.
If you delete a patient from the database, Django will automatically delete all appointments linked to that patient.

Example in real life:
A patient can book multiple appointments, but each appointment record is linked to a single specific patient.
'''
