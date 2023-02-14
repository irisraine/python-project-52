from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserForm
from .mixins import UserPermissionMixin


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")
    success_message = _('User is successfully registered')


class UserUpdateView(SuccessMessageMixin, UserPermissionMixin, UpdateView):
    template_name = 'users/user_update.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('User is successfully changed')
    permission_error_message = _("You don't have permission to change another user.")


class UserDeleteView(SuccessMessageMixin, UserPermissionMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    success_url = reverse_lazy('users_list')
    success_message = _('User is successfully deleted')
    permission_error_message = _("You don't have permission to delete another user.")
