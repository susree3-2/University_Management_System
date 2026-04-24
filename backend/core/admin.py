from django.contrib import admin
from .models import Course, Room, TimeSlot, Schedule

# Register all models so they appear in Django admin panel
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(Schedule)
