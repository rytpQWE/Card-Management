from django.forms import forms

from cards.models import History


class AddHistoryData(forms.ModelForm):
    class Meta:
        model = History
        fields = ['use_time', 'user']
