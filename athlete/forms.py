from django.forms import ModelForm
from .models import Athlete, Subscription


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

