from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from apps.user_profile.models import Patient, Employee

class Appointment(models.Model):
    date = models.DateTimeField(verbose_name='Appointment Date and time')
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='doctor')
    reason = models.TextField(blank=True, null=True, verbose_name='Reason for visit')
    notes = models.TextField(blank=True, null=True, verbose_name='Appointment notes')

    def __str__(self):
        return "Patient - {} Doc- {} At {}".format(self.patient, self.doctor, self.date)

class Session(models.Model):
    appointment = models.OneToOneField(to=Appointment, on_delete=models.CASCADE)
    checkin_time = models.TimeField(verbose_name='Checkin time')
    checkout_time = models.TimeField(blank=True, null=True, verbose_name='Checkout Time')
    symptoms = models.CharField(blank=True, null=True, max_length=200)
    notes = models.TextField(blank=True, null=True, verbose_name='Session notes')
    

class Vitals(models.Model):
    session = models.OneToOneField(to=Appointment, on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Body temperature')
    pulse_rate = models.FloatField(verbose_name='Pulse rate')
    respiration_rate = models.FloatField(verbose_name='Respiration rate')
    blood_pressure = models.FloatField(verbose_name='Blood pressure')
