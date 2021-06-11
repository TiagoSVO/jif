from django.contrib import admin
from .models import BloodType


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    pass
