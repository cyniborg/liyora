from django.db import models
from liyoura.modelsmeta import Meta
import uuid
from django.contrib.auth import get_user_model
from django.conf import settings

class Service_Providers(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=512)
    bio = models.CharField(max_length=10000, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    tiktok = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    x = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    work_email = models.CharField(max_length=64)
    work_phone = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = "Service Providers"
