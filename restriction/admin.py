from django.contrib import admin
from .models import Restriction


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    pass
