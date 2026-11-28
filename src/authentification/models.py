from django.contrib.auth.models import AbstractUser
from django.db import models


class FinanceUser(AbstractUser):

    country = models.CharField(
        max_length=100,
        default="France"
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    country = models.CharField(max_length=100, default="France")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    totp_secret = models.CharField(max_length=64, blank=True, default="")
    riskProfile = {1, 2, 3, 4, 5}

class Institution(models.Model):
    TYPE_CHOICES = [
        ("bank", "Bank"),
        ("broker", "Broker"),
        ("insurer", "Insurer"),
        ("asset_manager", "Asset management company"),
        ("fintech", "FinTech platform"),
    ]

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="France")
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
