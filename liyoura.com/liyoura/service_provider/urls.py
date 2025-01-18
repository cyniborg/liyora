from django.urls import path
from . import views
# This is where it is decided which view (logic) will be called for a particular URL
urlpatterns = [
    path('', views.providers_list, name='psychologists_list'),
    path('profile/<uuid:id>/', views.provider_profile, name='psychologist_profile'),
]