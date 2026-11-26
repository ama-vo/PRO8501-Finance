from django import forms
from .models import (
    CurrentAccount, SavingAccount, TaxWrapper, 
    Security, PrivateEquity, Cryptocurrency, Furniture, RealEstate
)

class CurrentAccountForm(forms.ModelForm):
    class Meta:
        model = CurrentAccount
        fields = ['name', 'Opendate', 'devise', 'value', 'interest_rate']

class SavingAccountForm(forms.ModelForm):
    class Meta:
        model = SavingAccount
        fields = ['name', 'Opendate', 'devise', 'value', 'is_regulate', 'ceilling', 'gross_rate', 'net_rate']

class TaxWrapperForm(forms.ModelForm):
    class Meta:
        model = TaxWrapper
        fields = ['name', 'Opendate', 'devise', 'value', 'subscription_date', 'cash_balance']

class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['name', 'Opendate', 'devise', 'value', 'ticker_code', 'shares_count', 'security_type', 'taxwrapper_link']

class PrivateEquityForm(forms.ModelForm):
    class Meta:
        model = PrivateEquity
        fields = ['name', 'Opendate', 'devise', 'value', 'codeLEI', 'numberFundUnit']

class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'Opendate', 'devise', 'value', 'codeSlugCoinGecko', 'numberFundUnit']

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'Opendate', 'devise', 'value', 'BuyingDate', 'address', 'sellingPrice']

class RealEstateForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['name', 'Opendate', 'devise', 'value', 'address', 'sellingPrice']