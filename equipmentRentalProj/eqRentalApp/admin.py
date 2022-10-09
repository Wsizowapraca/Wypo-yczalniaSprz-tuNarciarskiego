from django.contrib import admin

from .models import User, Equipment, Rent

# Register your models here.
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Rent)