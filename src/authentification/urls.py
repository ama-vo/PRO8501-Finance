from django.urls import path

from . import views

urlpatterns = [
    path("", views.totp_verify, name="totp_verify"),
    path("cancel/", views.cancel_totp, name="cancel_totp"),
]
