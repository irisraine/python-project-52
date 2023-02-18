from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class AuthorizationMixin(LoginRequiredMixin):
    login_url = 'login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _("AuthorizationRequired"))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
