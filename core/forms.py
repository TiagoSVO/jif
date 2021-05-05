from django.forms import ModelForm, ModelMultipleChoiceField
from .models import JIF, Athlete, Modality, Team, Championship, JIFsTeam


class JIFForm(ModelForm):
    modalities = ModelMultipleChoiceField(queryset=Modality.objects.all(), required=False)
    teams = ModelMultipleChoiceField(queryset=Team.objects.all(), required=False)

    class Meta:
        model = JIF
        # fields = ['title', 'year', 'edition', 'date_init', 'date_end']
        fields = '__all__'


class ChampionshipForm(ModelForm):
    teams = ModelMultipleChoiceField(queryset=JIFsTeam.objects.all(), required=False)

    class Meta:
        model = Championship
        fields = '__all__'


class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        exclude = ['updater_profile']

