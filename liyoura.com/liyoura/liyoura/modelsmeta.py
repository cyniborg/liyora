from django.db import models

class Meta(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=32)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True
