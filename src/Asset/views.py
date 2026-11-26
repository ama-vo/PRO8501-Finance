from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Asset.forms import CryptocurrencyForm, CurrentAccountForm, FurnitureForm, PrivateEquityForm, RealEstateForm, SavingAccountForm, SecurityForm, TaxWrapperForm
from .models import Asset, CurrentAccount


ASSET_FORMS = {
    'Ca': CurrentAccountForm,
    'Sa': SavingAccountForm,
    'Tw': TaxWrapperForm,
    'Sc': SecurityForm,
    'Pe': PrivateEquityForm,
    'Cry': CryptocurrencyForm,
    'Pp': FurnitureForm,
    'Re': RealEstateForm,
}


templates_map = {
            'Ca': 'asset_type_attributs/current_account.html',
            'Sa': 'asset_type_attributs/saving_account.html',
            'Tw': 'asset_type_attributs/tax_wrapper.html',
            'Sc': 'asset_type_attributs/security.html',
            'Pe': 'asset_type_attributs/private_equity.html',
            'Cry': 'asset_type_attributs/cryptocurrency.html',
            'Pp': 'asset_type_attributs/furniture.html',
            'Re': 'asset_type_attributs/real_estate.html',

        }

@login_required
def homePageAsset(request):


    if request.headers.get("HX-Request"):
        asset_type = request.GET.get("asset_type")
        print(asset_type)
        if asset_type == "init":
            return HttpResponse("")

        else:
            template_name = templates_map.get(asset_type) 
            if template_name:
                return render(request, template_name)

        
    if request.method == "POST":

        asset_type = request.POST.get("asset_type")
        print(asset_type)
        form_class = ASSET_FORMS.get(asset_type)
        
        if form_class:
            
            form_info = form_class(request.POST)
            print(request.headers)
            if form_info.is_valid():

                asset = form_info.save(commit=False)
                asset.user = request.user
                asset.save()
                
                if request.headers.get("HX-Request"):

                    assets = request.user.actif.all()            
                    return render(request, "assetDescription.html", {"assets": assets})

        assets = request.user.actif.all()
        
        asset_types = Asset.Asset_Type
        currency = Asset.Devise.choices     
        context = {
                    "assets" : assets,
                    "asset_types" : asset_types,
                    "currency" : currency,
                }
        return render(request,"asset_homepage.html", context)
    
    assets = request.user.actif.all()
            
    asset_types = Asset.Asset_Type
    currency = Asset.Devise.choices     
    context = {
                        "assets" : assets,
                        "asset_types" : asset_types,
                        "currency" : currency,
                    }

    return render(request,"asset_homepage.html", context)