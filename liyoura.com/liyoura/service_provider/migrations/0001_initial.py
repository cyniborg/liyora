# Generated by Django 5.1.4 on 2025-01-15 16:13

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Providers',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=32)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=32)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_description', models.CharField(max_length=512)),
                ('bio', models.CharField(blank=True, max_length=10000, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('x', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('work_email', models.CharField(max_length=64)),
                ('work_phone', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Service Providers',
            },
        ),
    ]
