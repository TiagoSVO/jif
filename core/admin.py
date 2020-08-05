from django.contrib import admin
from .models import JIFB


@admin.register(JIFB)
class JIFBAdmin(admin.ModelAdmin):
    pass
