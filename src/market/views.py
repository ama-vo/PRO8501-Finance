from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .services import get_history


@require_GET
def stock_history(request, symbol):
    """Renvoie l'historique d'un ticker en JSON : /market/api/history/AAPL/?period=1y"""
    period = request.GET.get("period", "1y")

    try:
        data = get_history(symbol, period)
    except ValueError as e:
        # Période inconnue : la requête du client est mauvaise (400)
        return JsonResponse({"error": str(e)}, status=400)

    if data is None:
        # Ticker inconnu chez Yahoo : rien à renvoyer (404)
        return JsonResponse({"error": f"Ticker introuvable : {symbol}"}, status=404)

    return JsonResponse(data)
