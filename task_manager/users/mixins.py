from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _


class UserPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.pk == self.get_object().pk or self.request.user.is_superuser

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, _("You aren't authorized! Please log in."))
            return redirect('login')
        messages.error(self.request, self.permission_denial_message)
        return redirect('users_list')
