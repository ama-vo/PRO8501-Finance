from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FinanceUser
from Asset import models

# Register your models here.
admin.site.register(FinanceUser, UserAdmin)
admin.site.register(models.Asset)
