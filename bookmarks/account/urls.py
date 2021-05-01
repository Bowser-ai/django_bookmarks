from django.contrib.auth.views import LoginView
from django.urls import path

from account.views import Dashboard, CustomLogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
