from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("First name"),
        widget=forms.TextInput(attrs={'placeholder': _('First name')}),
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("Last name"),
        widget=forms.TextInput(attrs={'placeholder': _('Last name')}),
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = _(
            'Password should contain at least 3 characters'
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
