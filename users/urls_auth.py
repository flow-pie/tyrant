from django.urls import  path

from wallet.urls import urlpatterns
from .views import (
    RegisterView, CustomLoginView,
    request_password_reset, confirm_password_reset
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', CustomLoginView.as_view()),
    path('password-reset/request', request_password_reset),
    path('password-reset/confirm', confirm_password_reset),
]