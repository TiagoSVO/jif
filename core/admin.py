from django.contrib import admin
from .models import JIFB, Phone, Dept


@admin.register(JIFB)
class JIFBAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'edition', 'date_init', 'date_end']


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    pass
