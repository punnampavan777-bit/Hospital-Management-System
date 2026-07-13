from django import forms
from django.contrib.auth.models import User
from .models import Patient

class PatientRegisterForm(forms.ModelForm):
    username = forms.CharField() # Optional
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean() # returns dict
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match...") 



# (OR) 

# from django import forms
# from django.contrib.auth.models import User

# class PatientRegisterForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
          
          #Optional (does automatically for User model)
#         username = cleaned_data.get("username")
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Username already taken")
#         return cleaned_data


#Note:
# super().clean():
# It returns a dictionary (dict) of cleaned form data for all fields that have passed individual validation.

# clean() method

# The clean() method in a Django ModelForm is used to implement custom validation logic that involves 
# multiple fields or depends on model-level constraints — logic that can not be handled by individual field 
# validators or clean_<field>() methods.


# Username already exists check is handled automatically by Django’s ModelForm system 
# (based on the model’s unique=True constraint).You do not need to add extra code for that.

# Since your form is a ModelForm for the User model and you’ve included the username field 
# in Meta.fields, Django will automatically validate unique constraints defined on the model.