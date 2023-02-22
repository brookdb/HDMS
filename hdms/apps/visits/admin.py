from django.contrib import admin
from .models import Appointment, Session

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['get_appointment_date', 'get_patient_name', ]


    def get_appointment_date(self, obj):
        return obj.date
    get_appointment_date.admin_order_field  = 'date'
    get_appointment_date.short_description = 'Appointment Date'  #Renames column head

    def get_patient_name(self, obj):
        return obj.patient.user.first_name
    get_patient_name.admin_order_field  = 'patient__user__first_name'
    get_patient_name.short_description = 'Patient Fist Name'

admin.site.register(Appointment, AppointmentAdmin)

class SessionAdmin(admin.ModelAdmin):
    model = Session
    list_display = ['get_appointment', 'get_checkin_time', ]


    def get_appointment(self, obj):
        return obj.appointment
    get_appointment.admin_order_field  = 'appointment'
    get_appointment.short_description = 'Appointment'  #Renames column head

    def get_checkin_time(self, obj):
        return obj.checkin_time
    get_checkin_time.admin_order_field  = 'checkin_time'
    get_checkin_time.short_description = 'Checkin Time'

admin.site.register(Session, SessionAdmin)
