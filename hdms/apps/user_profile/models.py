from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


BLOOD_GROUPS = [
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
]
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

JOB_CHOICES = [
    ('D', 'Doctor'),
    ('N', 'Nurse'),
    ('R', 'Receptionist'),
    ('HR', 'HR'),
    ('PR', 'Pharmacist')
]


#User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name='Address')
    phone = models.CharField(blank=True, null=True, max_length=20, verbose_name='Phone Number')
    ID_Card = models.ImageField(blank=True, null=True, upload_to='profile/img/')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    dob = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Date of Birth")


    def __str__(self):
        return self.user.email

    class Meta:
        abstract = True
        ordering = ['user']

class Patient(Profile):
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True, verbose_name="Blood Group")
    medical_history = models.TextField(blank=True, null=True, verbose_name='Medical History')
    curent_medications = models.TextField(blank=True, null=True, verbose_name='Current Medications')

class Employee(Profile):
    hire_date = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Hire Date")
    job_type = models.CharField(choices=JOB_CHOICES, max_length=2)
    job_title = models.CharField(blank=True, null=True, max_length=300, verbose_name='Job Title')
    department = models.CharField(blank=True, null=True, max_length=300, verbose_name='Department')
    manager = models.ManyToManyField('self', symmetrical=False, related_name='emplyoee_manager', blank=True)
    session_limit = models.IntegerField(blank=True, null=True, verbose_name='Daily Max hours')

    def is_doctor(self):
        if self.job_type == 'D':
            return True
        else:
            return False

    def is_nurse(self):
        if self.job_type == 'N':
            return True
        else:
            return False

    def is_receptionist(self):
        if self.job_type == 'R':
            return True
        else:
            return False

    def is_HR(self):
        if self.job_type == 'HR':
            return True
        else:
            return False
    def is_pharmacist(self):
        if self.job_type == 'PR':
            return True
        else:
            return False
