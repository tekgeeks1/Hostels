# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Location, Hostel,RoomType

admin.site.register(Location),
admin.site.register(Hostel),
admin.site.register(RoomType)

