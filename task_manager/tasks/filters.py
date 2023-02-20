from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status')
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor')
    )
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )
    current_user_tasks = BooleanFilter(
        method='get_current_user_tasks',
        label=_('CurrentUserOnly'),
        widget=forms.CheckboxInput,
    )

    def get_current_user_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
