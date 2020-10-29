from django.contrib import admin
from .forms import JIFForm
from .models import JIF, JIFsEvent, Committee, Dept, DeptsPhone, Sex, BloodType
from .models import Championship, Game, Group, ModalityType, Modality, Restriction
from .models import JIFModality, JIFModalityRestriction, JIFModalityRestrictionValue


class JIFModalityInline(admin.StackedInline):
    model = JIF.modalities.through
    extra = 0


class JIFModalityRestrictionValueInline(admin.StackedInline):
    model = JIFModalityRestrictionValue
    extra = 0


class JIFModalityRestrictionInline(admin.StackedInline):
    model = JIFModalityRestriction
    extra = 0

    # TODO: Verificar ou desenvolver a possibilidade de colocar em stackedinline para colocar os valores
    # da para as restrições no mesmo formulário de restrições de modalidade
    # inlines = [JIFModalityRestrictionValue, ]


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
class JIFModalityAdmin(admin.ModelAdmin):
    inlines = [JIFModalityRestrictionInline, ]


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    pass


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
