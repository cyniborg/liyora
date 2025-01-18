from django.urls import path
from . import views
# This is where it is decided which view (logic) will be called for a particular URL
urlpatterns = [
    path('', views.index, name='index'),
]