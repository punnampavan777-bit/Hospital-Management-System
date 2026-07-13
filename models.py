from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    # patient_id=models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 


