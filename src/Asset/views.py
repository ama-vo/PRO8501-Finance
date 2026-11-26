from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Asset, CurrentAccount



@login_required
def homePageAsset(request):


    if request.headers.get("HX-Request"):
        asset_type = request.GET.get("asset_type")

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

        template_name = templates_map.get(asset_type)
        if template_name:
            return render(request, template_name)

    if request.method == "POST":

        print(request.POST)
        if request.POST.get("asset_type") == "Ca":

            CurrentAccount.objects.create(
                name=request.POST.get("name"),
                Opendate=request.POST.get("Opendate"),
                devise=request.POST.get("currency"),
                user=request.user,
                type=request.POST.get("asset_type"),
                interest_rate=request.POST.get("interest_rate")
            )   

    
    assets = request.user.actif.all()
    
    asset_types = Asset.Asset_Type
    currency = Asset.Devise 
    
    context = {
        "assets" : assets,
        "asset_types" : asset_types,
        "currency" : currency,
    }
    
    return render(request,"asset_homepage.html", context)