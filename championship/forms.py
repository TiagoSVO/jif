from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Championship
from team.models import JIFsTeam


class ChampionshipForm(ModelForm):
    teams = ModelMultipleChoiceField(queryset=JIFsTeam.objects.all(), required=False, label='Times')

    class Meta:
        model = Championship
        fields = '__all__'
