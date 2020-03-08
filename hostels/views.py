# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def Home(request):
    locations = Location.objects.all()
    return render(request, 'hostels/locations.html', {'locations':locations})

def HostelRooms(request, hostel):
    # return HttpResponse(hostel)
    hostel = Hostel.objects.get(name=hostel)
    return render(request, 'hostels/rooms.html', {'hostel':hostel} )


def LocHostels(request, location):
    hostel = Hostel.objects.filter(location__name=location)
    return render(request, 'hostels/HostelsInLocation.html', {'hostel':hostel} )



    
    