# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='location')
    
    def __str__(self):
         return self.name
     
    def snippet(self):
         return self.description[:200]+ '...'
    
    
class RoomType(models.Model):
     roomType  = (
          ('1 in 1', '1 in 1'),
          ('2 in 1', '2 in 1'),
          ('3 in 1', '3 in 1'),
          ('4 in 1', '4 in 1'),
     ) 
     roomtype = models.CharField(blank=True, null=True, max_length=100, choices =roomType)
     price = models.IntegerField(blank=True, null=True)
     
     def __str__(self):
         return self.roomtype


class Hostel(models.Model):
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='hostel')
    
    roomtype1 =  models.ForeignKey(RoomType,blank=True, null=True, related_name = 'OneInOne')
    roomtype2 =  models.ForeignKey(RoomType,blank=True, null=True, related_name = 'TwoInOne')
    roomtype3 =  models.ForeignKey(RoomType,blank=True, null=True, related_name = 'ThreeInOne')
    roomtype4 =  models.ForeignKey(RoomType,blank=True, null=True, related_name = 'FourInOne')
    
     
    def __str__(self):
         return self.name

     
    def snippet(self):
         return self.description[:200]+ '...'


    
# class BookRoom(models.Model):
#      user = models.ForeignKey(User, on_delete=models.CASCADE)
#      hostel = models.ForeignKey(Hostel,null=True, on_delete=models.CASCADE)
#      def __str__(self):
#          return self.user
     