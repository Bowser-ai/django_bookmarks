from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class Dashboard(LoginRequiredMixin, View):
    template_name = 'account/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'section': 'dashboard'})
