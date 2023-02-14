from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserForm


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")
    success_message = _('User is successfully registered')
