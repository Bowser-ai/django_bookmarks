from django.contrib.auth.views import LoginView

from account.forms import LoginForm


class UserLogin(LoginView):
    template_name = 'account/login.html'

