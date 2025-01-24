from django.shortcuts import render, get_object_or_404, redirect
from .models import Service_Providers
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import PsychologistProfileForm
from datetime import datetime
from pprint import pprint
# Create your views here.

def providers_list(request):
    psychologists = get_list_or_404(Service_Providers, active=True)
    return render(request, 'service_providers/providers_list.html', {'providers': psychologists})

def provider_profile(request, id):
    psychologist = get_object_or_404(Service_Providers, id=id)
    return render(request, 'service_providers/provider_profile.html', {'provider': psychologist})

@login_required
def provider_profile_edit(request, id):
    user = request.user
    psychologist = get_object_or_404(Service_Providers, id=id)
    if request.method == 'GET':
        return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})
        # check if the user has the manager role for this psychologist and allow editing
        '''if psychologist.user.username == user.username or user.is_superuser:
            return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})
        else:
            return redirect('psychologist_profile', id=id)'''
    '''elif request.method == 'POST':
        service_provider_form = PsychologistProfileForm(request.POST, instance=psychologist);
        if service_provider_form.is_valid():
            service_provider_form.save(commit=False)
            service_provider_form.updated_by = user.username
            service_provider_form.save()
            
            return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})
        else:
            return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist, 'form': service_provider_form})'''

@login_required
def provider_self_edit(request):
    user = request.user
    psychologist = get_object_or_404(Service_Providers, user=user)
    return render(request, 'service_providers/provider_profile_edit.html', {'provider': psychologist})
