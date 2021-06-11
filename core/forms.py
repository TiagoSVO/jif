from django.forms import ModelForm, ModelMultipleChoiceField
from .models import JIF
from modality.models import Modality
from team.models import Team


class JIFForm(ModelForm):
    modalities = ModelMultipleChoiceField(queryset=Modality.objects.all(), required=False, label='Modalidades')
    teams = ModelMultipleChoiceField(queryset=Team.objects.all(), required=False, label='Times')

    class Meta:
        model = JIF
        # fields = ['title', 'year', 'edition', 'date_init', 'date_end']
        fields = '__all__'

