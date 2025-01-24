from django import forms
from .models import Service_Providers

class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = Service_Providers
        fields = "__all__"
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by', 'user']
