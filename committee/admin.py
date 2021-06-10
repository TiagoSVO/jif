from django.contrib import admin
from .models import Committee, FunctionTypeCommittee


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(CommitteeAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['jif']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


@admin.register(FunctionTypeCommittee)
class FunctionTypeCommitteeAdmin(admin.ModelAdmin):
    pass
