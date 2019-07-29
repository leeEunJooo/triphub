# Admin urls.py

from django.contrib import admin
from django.urls import path , include
import TripHubApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TripHubApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('Rooms/', include('Rooms.urls')),
    path('select/', include('place_select.urls')),
]
