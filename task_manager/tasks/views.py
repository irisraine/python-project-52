from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthorizationMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .filters import TaskFilter
from .models import Task
from .forms import TaskForm


class TaskListView(AuthorizationMixin, FilterView):
    template_name = 'tasks/tasks_list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    ordering = ['pk']


class TaskDetailView(AuthorizationMixin, DetailView):
    template_name = 'tasks/task.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(SuccessMessageMixin, AuthorizationMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks_list")
    success_message = _('TaskCreateSuccess')
    extra_context = {
        'category': _("Tasks"),
        'title_action': _("TaskCreate"),
        'button': _("ButtonCreate")
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, AuthorizationMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('TaskUpdateSuccess')
    extra_context = {
        'category': _("Tasks"),
        'title_action': _("TaskUpdate"),
        'button': _("Update")
    }


class TaskDeleteView(SuccessMessageMixin, AuthorizationMixin, DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('tasks_list')
    success_message = _('TaskDeleteSuccess')
    extra_context = {
        'category': _("Tasks"),
        'title_action': _("TaskDelete")
    }
