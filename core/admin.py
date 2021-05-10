from django.contrib import admin
from .forms import JIFForm, AthleteForm, ChampionshipForm, SubscriptionForm
from .models import JIF, JIFsEvent, Committee, Dept, DeptsPhone, Sex, BloodType, Team, TeamStatus
from .models import Championship, Game, Group, ModalityType, Modality, Restriction, ScoreType
from .models import JIFModality, JIFModalityRestriction, JIFModalityRestrictionValue, Athlete
from .models import Subscription
from nested_admin import NestedModelAdmin, NestedStackedInline


class JIFModalityRestrictionValueInline(NestedStackedInline):
    model = JIFModalityRestrictionValue
    extra = 0


class JIFModalityRestrictionInline(NestedStackedInline):
    model = JIFModalityRestriction
    extra = 0

    # TODO: Verificar ou desenvolver a possibilidade de colocar em stackedinline para colocar os valores
    # da para as restrições no mesmo formulário de restrições de modalidade
    inlines = [JIFModalityRestrictionValueInline, ]


@admin.register(JIF)
class JIFAdmin(admin.ModelAdmin):
    form = JIFForm
    list_display = ['title', 'year', 'edition', 'date_init', 'date_end']


@admin.register(JIFsEvent)
class JIFsEventAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(JIFsEventAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['jif']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


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


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    pass


@admin.register(DeptsPhone)
class DeptsPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    pass


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ModalityType)
class ModalityTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Modality)
class ModalityAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModalityAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['modality_type', 'sex']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


@admin.register(JIFModality)
class JIFModalityAdmin(NestedModelAdmin):
    inlines = [JIFModalityRestrictionInline, ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(JIFModalityAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['modality', 'jif']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


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


@admin.register(ScoreType)
class ScoreTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


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
