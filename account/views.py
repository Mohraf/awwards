from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse_lazy

from braces import views

from .models import User, Connection
from .forms import SignUpForm, UpdateAccountForm, LoginForm, ChangePasswordForm
from .helpers import get_current_user


class DetailAccountView(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'accounts/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailAccountView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        context['username'] = username

        context['user'] = get_current_user(self.request)

        return


class UpdateAccountView(
        views.LoginRequiredMixin,
        views.FormValidMessageMixin,
        generic.UpdateView
):
    model = User
    form_valid_message = 'Successfully updated your account.'
    form_class = UpdateAccountForm
    template_name = 'accounts/account_form.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
