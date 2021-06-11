from django.contrib import admin

from .forms import AthleteForm, SubscriptionForm
from .models import Athlete, Subscription


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    form = AthleteForm
    list_display = ['first_name', 'last_name', 'cpf', 'birth_date', 'email']
    list_display_links = ['first_name', 'last_name', 'cpf']
    list_editable = ['birth_date', 'email']

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(AthleteAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['sex', 'dept', 'blood_type']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form

    # TODO: Ajustando o salvamento automático do userjisprofile no campo updater_profile. No userjif model tem a resp.
    #
    # def save_model(self, request, obj, form, change):
    #     obj.updater_profile = request.user.jifuserprofile_set.all()[0]
    #     #TODO: Verificar se tal perfil pode realizar esta ação
    #     super().save_model(request, obj, form, change)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    form = SubscriptionForm
    list_display = ['jif_team', 'athlete', 'created_at', 'updated_at']

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(SubscriptionAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['athlete']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form

