from django.contrib import admin
from .models import TeamStatus, Team


@admin.register(TeamStatus)
class TeamStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(TeamAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['modality', 'dept', 'sex', 'team_status']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form
