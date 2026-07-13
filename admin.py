from django.contrib import admin
from .models import Doctor

class AdminDoctor(admin.ModelAdmin):
    list_display=[ "name", "available_date", "available_time", "specialization" ]

admin.site.register(Doctor,AdminDoctor)
