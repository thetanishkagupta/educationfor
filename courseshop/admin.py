from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import extendeduser
from .models import Order
admin.site.register(extendeduser)
admin.site.register(Order)
