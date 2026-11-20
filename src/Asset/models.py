from django.db import models
from authentification.models import FinanceUser 



class Asset(models.Model):

    class Asset_Type(models.TextChoices):
        CC = 'Current Account', 'Cash' 
        LB = 'Savings Accounts'
        EF = 'Tax Wrappers' 
        AC = 'Stocks' 
        PE = 'Private Equity'
        CRY = 'Cryptocurrency'
        MOB = 'Personal Property' 
        IMO = 'Real Estate'


    class Devise(models.TextChoices):
        EUR = 'Euro', '€'
        USD = 'US Dollar', '$'
        GBP = 'British Pound', '£'
        JPY = 'Japanese Yen', '¥'
        CHF = 'Swiss Franc', 'CHF' 
        CAD = 'Canadian Dollar', 'CA$' 
            

    type = models.CharField(max_length=19, choices=Asset_Type)
    Opendate = models.DateField()
    Closedate = models.DateField(blank=True, null=True)
    value = models.IntegerField(default=0)
    devise = models.CharField(choices=Devise, default=Devise.EUR)
    user = models.ForeignKey( FinanceUser, on_delete=models.CASCADE, related_name="actif")


class CurrentAccount(Asset):

    interest_rate = models.IntegerField(blank=True, null=True)

class SavingAccount(Asset):

    is_regulate = models.BooleanField()
    ceilling = models.IntegerField()
    gross_rate = models.IntegerField() 
    net_rate = models.IntegerField()

class TaxWrapper(Asset):

    class TaxWrapper_Type(models.TextChoices):

        PEA = 'Equity Savings Plan'
        CTO = 'Ordinary Securities Account'
        LI = 'Life Insurance'
        PER = 'Retirement Savings Plan'

    subscription_date = models.DateField()
    cash_balance = models.IntegerField()

class Security(Asset):

    class Securities_Type(models.TextChoices):

        SS = 'Single Stock'
        ETF = 'Exchange Traded Fund'
        BO = 'Bond' 
    ticker_code = models.CharField(max_length=12)
    shares_count = models.IntegerField()
    security_type = models.CharField(choices=Securities_Type)
    taxwrapper_link = models.ForeignKey(TaxWrapper,on_delete=models.CASCADE, related_name='security' )
