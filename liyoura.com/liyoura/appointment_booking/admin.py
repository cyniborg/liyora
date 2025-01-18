from django.contrib import admin
from .models import Appointment_Services, Customers, Holidays, Service_Availabilities, Appointments

admin.site.register(Appointment_Services)
admin.site.register(Customers)
admin.site.register(Holidays)
admin.site.register(Service_Availabilities)
admin.site.register(Appointments)
