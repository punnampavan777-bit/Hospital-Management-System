from django.shortcuts import render
from doctors.models import Doctor

def show_doctors(request):
    qs=Doctor.objects.all()
    return render(request,"show_doctors.html",{"qs": qs})from django.shortcuts import render

# Create your views here.
