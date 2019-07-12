from django.shortcuts import render
from .models import TripHub



def index(request):

    triphub = TripHub

    return render(request,'index.html' ,  {'triphub' :triphub})
