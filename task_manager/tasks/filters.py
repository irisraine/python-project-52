from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=_('AnyStatus')
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=_('AnyExecutor')
    )
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=_('AnyLabel')
    )
    self_tasks = BooleanFilter(
        method='get_self_tasks',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def get_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
