from django.contrib import admin
from .models import ModalityGrouping, ModalityType, Modality, JIFModality, ScoreType
from restriction.models import JIFModalityRestriction, JIFModalityRestrictionValue

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


@admin.register(ScoreType)
class ScoreTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ModalityGrouping)
class ModalityGroupingAdmin(admin.ModelAdmin):
    pass


@admin.register(ModalityType)
class ModalityTypeAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModalityTypeAdmin, self).get_form(request, obj, **kwargs)
        disable_related_crud = ['score_type']

        for field_name in disable_related_crud:
            field = form.base_fields[field_name]
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
        return form


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
