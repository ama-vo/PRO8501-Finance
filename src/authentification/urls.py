from django.urls import path

from . import views

urlpatterns = [
    path("", views.otp, name="otp"),
    # Name that allauth redirects to once the code has been sent.
    path("", views.otp, name="account_confirm_login_code"),
]
