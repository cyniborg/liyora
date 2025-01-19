from django.shortcuts import render, get_object_or_404
from .models import Service_Providers
from django.shortcuts import get_list_or_404
from pprint import pprint
# Create your views here.
def providers_list(request):
    psychologists = get_list_or_404(Service_Providers, active=True)
    return render(request, 'service_providers/providers_list.html', {'providers': psychologists})

def provider_profile(request, id):
    psychologist = get_object_or_404(Service_Providers, id=id)
    return render(request, 'service_providers/provider_profile.html', {'provider': psychologist})

def provider_profile_edit(request, id):
    # This should only be based on the logged in user id
    psychologist = get_object_or_404(Service_Providers, id=id)
    return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})

def provider_profile_update(request, id):
    # psychologist = get_object_or_404(Service_Providers, id=id)
    # return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})
    print(request.POST)