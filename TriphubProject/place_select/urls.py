# place_select urls.py
from django.urls import path
from .views import place_select ,attraction ,attraction2, next_select_page, map_marker

urlpatterns = [
    path('place_select/' , place_select , name = "place_select"),
    path('attraction/', attraction , name = "attraction" ),
    path('attraction2/', attraction2 , name ="attraction2"),
    path('next_select_page/', next_select_page, name = "next_select_page"),
    path('', map_marker , name = "map_marker"),
]   
