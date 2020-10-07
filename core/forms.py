from django.forms import ModelForm, ModelMultipleChoiceField
from .models import JIF, Modality


class JIFForm(ModelForm):
    modalities = ModelMultipleChoiceField(queryset=Modality.objects.all())

    class Meta:
        model = JIF
        fields = ['title', 'year', 'edition', 'date_init', 'date_end', 'modalities']
