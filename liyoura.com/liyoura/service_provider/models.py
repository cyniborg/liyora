from django.db import models
from liyoura.modelsmeta import Meta
import uuid
from django.contrib.auth import get_user_model
from django.conf import settings

# Update to postgres instead of sqlite
class Service_Providers(Meta):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=512)
    bio = models.CharField(max_length=10000, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    tiktok = models.URLField(max_length=255, null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    x = models.URLField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    youtube = models.URLField(max_length=255, null=True, blank=True)
    work_email = models.EmailField(max_length=64)
    work_phone = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = "Service Providers"
