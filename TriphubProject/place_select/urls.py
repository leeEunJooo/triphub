# place_select urls.py
from django.urls import path
from place_select.views import place_select ,attraction ,attraction2, next_select_page 

urlpatterns = [
    path('place_select/' , place_select , name = "place_select"),
    path('attraction/', attraction , name = "attraction" ),
    path('attraction2/', attraction2 , name ="attraction2"),
    path('next_select_page/', next_select_page, name = "next_select_page"),
]   
