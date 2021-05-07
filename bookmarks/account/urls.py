from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from account.views import Dashboard, CustomLogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset/<uid64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
