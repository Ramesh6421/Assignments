from django.shortcuts import render
from newApp.models import Passenger
# Create your views here.

def passenger(request):
    passenger = Passenger.objects.all()
    context = {
        'passenger':passenger
    }
    return render(request,'newApp/pgr.html',context)