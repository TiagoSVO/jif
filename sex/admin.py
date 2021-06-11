from django.contrib import admin
from .models import Sex


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    pass
