from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import AuthorizationMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm


class StatusListView(AuthorizationMixin, ListView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(SuccessMessageMixin, AuthorizationMixin, CreateView):
    template_name = 'statuses/status_create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy("statuses_list")
    success_message = _('StatusCreateSuccess')


class StatusUpdateView(SuccessMessageMixin, AuthorizationMixin, UpdateView):
    template_name = 'statuses/status_update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('StatusUpdateSuccess')


class StatusDeleteView(SuccessMessageMixin, AuthorizationMixin, DeleteView):
    template_name = 'statuses/status_delete.html'
    model = Status
    success_url = reverse_lazy('statuses_list')
    success_message = _('StatusDeleteSuccess')
