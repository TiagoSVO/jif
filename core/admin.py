from django.contrib import admin
from .forms import JIFForm, AthleteForm, ChampionshipForm
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
    pass


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    pass


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
    pass


@admin.register(JIFModality)
class JIFModalityAdmin(NestedModelAdmin):
    inlines = [JIFModalityRestrictionInline, ]


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


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


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

    # TODO: Ajustando o salvamento automático do userjisprofile no campo updater_profile. No userjif model tem a resp.
    #
    # def save_model(self, request, obj, form, change):
    #     obj.updater_profile = request.user.jifuserprofile_set.all()[0]
    #     #TODO: Verificar se tal perfil pode realizar esta ação
    #     super().save_model(request, obj, form, change)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
