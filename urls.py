from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('view/', views.view_appointments, name='view_appointments'),
]
