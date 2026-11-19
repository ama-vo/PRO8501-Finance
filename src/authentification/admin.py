from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FinanceUser

# Register your models here.
admin.site.register(FinanceUser, UserAdmin)