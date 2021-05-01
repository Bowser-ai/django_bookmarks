from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import View


class CustomLogoutView(View):
    template_name = 'registration/_logged_out.html'

    def get(self, request, *arg, **kwargs):
        logout(request)
        return render(request, self.template_name)
