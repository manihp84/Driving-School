from django.contrib import admin

# Register your models here.

from .models import Instructor, Booking, Payment

admin.site.register(Instructor)
admin.site.register(Booking)
admin.site.register(Payment)

