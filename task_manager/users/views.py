from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserForm
from task_manager.mixins import AuthorizationMixin, UserPermissionMixin


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")
    success_message = _('UserCreateSuccess')


class UserUpdateView(SuccessMessageMixin, AuthorizationMixin,
                     UserPermissionMixin, UpdateView):
    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('UserUpdateSuccess')
    permission_denial_message = _("UserUpdateDenial")
    extra_context = {
        'category': _("Users"),
        'title_action': _("UserUpdate"),
        'button': _("Update")
    }


class UserDeleteView(SuccessMessageMixin, AuthorizationMixin,
                     UserPermissionMixin, DeleteView):
    template_name = 'delete.html'
    model = User
    success_url = reverse_lazy('users_list')
    success_message = _('UserDeleteSuccess')
    permission_denial_message = _("UserDeleteDenial")
    extra_context = {
        'category': _("Users"),
        'title_action': _("UserDelete")
    }

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        if user.author.all() or user.executor.all():
            messages.error(self.request, _("UserOnTaskDeleteDenial"))
            return redirect('/users/')
        else:
            return super().post(self, request, *args, **kwargs)
