from django.contrib import admin
from .models import Appointment
# Register your models here.
class AdminAppointment(admin.ModelAdmin):
    list_display=["patient","name","age","contact","decease","doctor"]

admin.site.register(Appointment,AdminAppointment)
