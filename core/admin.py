from django.contrib import admin
from .models import JIF, JIFsEvent, Committee, Dept, DeptsPhone, Sex, BloodType
from .models import Championship, Game, Group, ModalityType, Modality


@admin.register(JIF)
class JIFAdmin(admin.ModelAdmin):
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


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
