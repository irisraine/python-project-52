from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        label=_("Name"),
        widget=forms.TextInput(attrs={'placeholder': _('Name')}),
    )

    class Meta:
        model = Status
        fields = ('name', )
