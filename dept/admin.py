from django.contrib import admin
from .models import Dept, DeptsPhone


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    pass


@admin.register(DeptsPhone)
class DeptsPhoneAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(DeptsPhoneAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['dept']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form
