from django.contrib import admin
from .forms import JIFForm, AthleteForm, ChampionshipForm, SubscriptionForm
from .models import JIF, Team, TeamStatus
from .models import Championship, Game, Group, Restriction, Athlete
from .models import Subscription
from nested_admin import NestedModelAdmin, NestedStackedInline


@admin.register(JIF)
class JIFAdmin(admin.ModelAdmin):
    form = JIFForm
    list_display = ['title', 'year', 'edition', 'date_init', 'date_end']


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    pass


class ChampionshipTeams(NestedStackedInline):
    model = Championship.teams.through
    extra = 0


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    form = ChampionshipForm
    filter_vertical = ('teams',)
    list_display = ['title', 'jif_modality', 'started_at', 'finished_at']
    list_display_links = ['title', 'jif_modality']
    list_editable = ['started_at', 'finished_at']

    def get_form(self, request, obj=None, **kwargs):
        championship_form = super(ChampionshipAdmin, self).get_form(request, obj, **kwargs)
        field = championship_form.base_fields['jif_modality']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False

        return championship_form


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(GroupAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['championship']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


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
