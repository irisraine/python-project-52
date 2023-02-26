from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthorizationMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm


class StatusListView(AuthorizationMixin, ListView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    context_object_name = 'statuses'
    ordering = ['pk']


class StatusCreateView(SuccessMessageMixin, AuthorizationMixin, CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy("statuses_list")
    success_message = _('StatusCreateSuccess')
    extra_context = {
        'category': _("Statuses"),
        'title_action': _("StatusCreate"),
        'button': _("ButtonCreate")
    }


class StatusUpdateView(SuccessMessageMixin, AuthorizationMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('StatusUpdateSuccess')
    extra_context = {
        'category': _("Statuses"),
        'title_action': _("StatusUpdate"),
        'button': _("Update")
    }


class StatusDeleteView(SuccessMessageMixin, AuthorizationMixin, DeleteView):
    template_name = 'delete.html'
    model = Status
    success_url = reverse_lazy('statuses_list')
    success_message = _('StatusDeleteSuccess')
    extra_context = {
        'category': _("Statuses"),
        'title_action': _("StatusDelete")
    }

    def post(self, request, *args, **kwargs):
        status = Status.objects.get(id=kwargs['pk'])
        if status.task_set.all():
            messages.error(self.request, _("StatusOnTaskDeleteDenial"))
            return redirect('/statuses/')
        else:
            return super().post(self, request, *args, **kwargs)
