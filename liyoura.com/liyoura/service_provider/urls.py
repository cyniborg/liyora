from django.urls import path
from . import views
# This is where it is decided which view (logic) will be called for a particular URL
urlpatterns = [
    path('', views.providers_list, name='psychologists_list'),
    path('profile/<uuid:id>/', views.provider_profile, name='psychologist_profile'),
    path('profile/<uuid:id>/edit/', views.provider_profile_edit, name='psychologist_profile_edit'),
    path('profile/<uuid:id>/update/', views.provider_profile_update, name='psychologist_profile_update'),
]
