from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import views
from accounts.forms import LoginForm


class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('all_tasks')


class LogoutView(views.LogoutView):
    pass