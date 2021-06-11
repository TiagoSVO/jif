from django.contrib import admin
from .models import Championship, Game, Group
from .forms import ChampionshipForm

from nested_admin import NestedModelAdmin, NestedStackedInline


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

