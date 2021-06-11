from django.forms import ModelForm, ModelMultipleChoiceField
from .models import JIF, Athlete, Team, Championship, JIFsTeam, Subscription
from modality.models import Modality


class JIFForm(ModelForm):
    modalities = ModelMultipleChoiceField(queryset=Modality.objects.all(), required=False, label='Modalidades')
    teams = ModelMultipleChoiceField(queryset=Team.objects.all(), required=False, label='Times')

    class Meta:
        model = JIF
        # fields = ['title', 'year', 'edition', 'date_init', 'date_end']
        fields = '__all__'


class ChampionshipForm(ModelForm):
    teams = ModelMultipleChoiceField(queryset=JIFsTeam.objects.all(), required=False, label='Times')

    class Meta:
        model = Championship
        fields = '__all__'


class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)
        updater_profile_field = self.fields['updater_profile']
        current_user = self.Meta.formfield_callback.keywords['request'].user
        updater_profile_field.queryset = current_user.jifuserprofile_set.all()


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        updater_profile_field = self.fields['updater_profile']
        current_user = self.Meta.formfield_callback.keywords['request'].user
        updater_profile_field.queryset = current_user.jifuserprofile_set.all()

