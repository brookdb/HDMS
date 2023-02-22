from django.contrib import admin
from .models import Patient, Employee

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['get_email', 'get_user_fname', ]


    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field  = 'user__email'
    get_email.short_description = 'Email'  #Renames column head

    def get_user_fname(self, obj):
        return obj.user.first_name
    get_user_fname.admin_order_field  = 'user__first_name'
    get_user_fname.short_description = 'Fist Name'

# Register your models here.
admin.site.register(Patient, PatientAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['get_email', 'get_user_fname', ]


    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field  = 'user__email'
    get_email.short_description = 'Email'  #Renames column head

    def get_user_fname(self, obj):
        return obj.user.first_name
    get_user_fname.admin_order_field  = 'user__first_name'
    get_user_fname.short_description = 'Fist Name'

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
