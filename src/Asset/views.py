from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def homePageAsset(request):

    assets = request.user.actif.all()
    for asset in assets:
        print(asset.value)
    return render(request,"asset_homepage.html", {"assets": assets})