from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import get_history


@login_required(login_url="login")
def research(request):
    return render(request, "market/research.html")


@login_required(login_url="login")
@require_GET
def stock_history(request, symbol):
    period = request.GET.get("period", "1y")

    try:
        data = get_history(symbol, period)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    if data is None:
        return JsonResponse(
            {"error": f"Ticker not found: {symbol}"},
            status=404
        )

    return JsonResponse(data)

