from django.db import models
from liyoura.modelsmeta import Meta
import uuid
from django.contrib.auth import get_user_model
from django.conf import settings
from service_provider.models import Service_Providers

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted_user")[0]


class Holidays(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    short_description = models.CharField(max_length=256, null=False)
    month = models.IntegerField(null=False)
    day = models.IntegerField(null=False)
    full_day = models.BooleanField(default=False)
    start_time = models.IntegerField(default=900)
    end_time = models.IntegerField(default=1200)
    provider_id = models.ForeignKey(Service_Providers, on_delete=models.CASCADE)
    def __str__(self):
        return self.short_description
    class Meta:
        verbose_name_plural = "Holidays"
  
class Appointment_Services(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    provider_id = models.ForeignKey(Service_Providers, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=256, null=False)
    description = models.TextField(max_length=4000)
    duration = models.IntegerField(null=False)
    price = models.FloatField(default=0)
    def __str__(self):
        return self.short_description
    class Meta:
        verbose_name_plural = "Appointment Services"

class Service_Availabilities(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    service_id = models.ForeignKey(Appointment_Services, on_delete=models.CASCADE)
    day = models.IntegerField(null=False)
    start_time = models.IntegerField(default=900)
    end_time = models.IntegerField(default=1800)
    break_duration = models.IntegerField(default=0)
    break_start_time = models.IntegerField(default=1200)
    break_end_time = models.IntegerField(default=1300)
    def __str__(self):
        return self.day
    class Meta:
        verbose_name_plural = "Service Availabilities"

class Customers(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, null=False, unique=True)
    title = models.IntegerField(default=0)
    full_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Customers"

class Appointments(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.SET(get_sentinel_user))
    service_id = models.ForeignKey(Appointment_Services, on_delete=models.SET(get_sentinel_user))
    provider_id = models.ForeignKey(Service_Providers, on_delete=models.SET(get_sentinel_user))
    appointment_date = models.DateField(null=False)
    appointment_time = models.TimeField(null=False)
    status = models.IntegerField(default=0)
    notes = models.CharField(max_length=4000)
    def __str__(self):
        return self.appointment_date
    class Meta:
        verbose_name_plural = "Appointments"
