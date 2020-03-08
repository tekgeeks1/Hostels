from django.conf.urls import url
from . import views

app_name = 'hostels'
urlpatterns = [
    url(r'^locations/$', views.Home, name="hostelsHome"),  #rendering all locations for hostels
    url(r'^(?P<location>[\w-]+)/$', views.LocHostels, name="hostelsInLocation"), # rendering all hostels in a location
    url(r'^(?P<hostel>[\s\w-]+)/$', views.HostelRooms, name="roomsInHostel"), # renders rooms of a hostel for booking
    
]