from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Asset



@login_required
def homePageAsset(request):


    
    assets = request.user.actif.all()
    for asset in assets:
        print(asset.value)
    asset_types = Asset.Asset_Type
    
    context = {
        "assets" : assets,
        "asset_types" : asset_types
    }
    
    if request.headers.get("HX-Request") == "true":
        template = request.GET.get("asset_type")
        
        print(template)
        if template == "Sc":
            return render(request, 'asset_type_attributs/Stock.html')
    
    return render(request,"asset_homepage.html", context)