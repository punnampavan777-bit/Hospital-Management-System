from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PatientRegisterForm
from .models import Patient
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid(): 
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            Patient.objects.create(user=user)
            messages.success(request,"You have successfully registered. Now you can login.")
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'patients/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('book_appointment')
    return render(request,'patients\login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('home')



'''
Explanation:

 1) user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

This line creates a new user account in Django’s built-in authentication system.

create_user() is a helper method that creates a new User instance then hashes the password securely before 
saving it and saves the user  in database and it returns that new User object.

id	username	    password (hashed)	...
-------------------------------------------------------------------
1	Venu	             pbkdf2_sha256$...hash…	...

2) Patient.objects.create(user=user)

This line creates a new Patient record  and links it to that  specified user.
It adds a new row to your Patient table, linking it to the newly created User record.

id	user_id		...
---------------------------------
1		1		...

So effectively, these two steps together create:
i) A user account (to handle login/logout/authentication)
ii) A patient profile (to store additional patient-specific data tied to that user)

'''

