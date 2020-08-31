from django.contrib import admin
from .models import JIFB


@admin.register(JIFB)
class JIFBAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'edition', 'date_init', 'date_end']
