from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Asset



@login_required
def homePageAsset(request):

    assets = request.user.actif.all()
    for asset in assets:
        print(asset.value)
    asset_types = Asset.Asset_Type.values
    
    context = {
        "assets" : assets,
        "asset_types" : asset_types
    }
    
    return render(request,"asset_homepage.html", context)