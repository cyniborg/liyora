# Generated by Django 5.1.4 on 2025-01-13 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_booking', '0002_alter_customers_user_alter_service_providers_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment_services',
            options={'verbose_name_plural': 'Appointment Services'},
        ),
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='holidays',
            options={'verbose_name_plural': 'Holidays'},
        ),
        migrations.AlterModelOptions(
            name='service_availabilities',
            options={'verbose_name_plural': 'Service Availabilities'},
        ),
        migrations.AlterModelOptions(
            name='service_providers',
            options={'verbose_name_plural': 'Service Providers'},
        ),
    ]
