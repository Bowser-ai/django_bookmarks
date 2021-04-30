from django.urls import path

from account.views import UserLogin


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login')
]

