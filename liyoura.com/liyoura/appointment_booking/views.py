from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Service_Providers
from pprint import pprint
# Create your views here.
# This is where the logic for the appointment booking system will be implemented
def index(request):
    return HttpResponse("Hello, world. You're at the appointment_booking index.")
