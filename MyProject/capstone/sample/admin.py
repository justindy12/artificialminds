from django.contrib import admin

# Register your models here.

from .models import RoomMember
from .models import Room, Message

admin.site.register(RoomMember)
admin.site.register(Room)
admin.site.register(Message)