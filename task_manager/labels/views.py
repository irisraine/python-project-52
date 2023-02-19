from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthorizationMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Label
from .forms import LabelForm


class LabelListView(AuthorizationMixin, ListView):
    template_name = 'labels/labels_list.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, AuthorizationMixin, CreateView):
    template_name = 'labels/label_create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("labels_list")
    success_message = _('LabelCreateSuccess')


class LabelUpdateView(SuccessMessageMixin, AuthorizationMixin, UpdateView):
    template_name = 'labels/label_update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')
    success_message = _('LabelUpdateSuccess')


class LabelDeleteView(SuccessMessageMixin, AuthorizationMixin, DeleteView):
    template_name = 'labels/label_delete.html'
    model = Label
    success_url = reverse_lazy('labels_list')
    success_message = _('LabelDeleteSuccess')

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(id=kwargs['pk'])
        if label.task_set.all():
            messages.error(self.request, _("LabelOnTaskDeleteDenial"))
            return redirect('/labels/')
        else:
            return super().post(self, request, *args, **kwargs)
