import yfinance as yf

PERIODS = {
    "7d": "1m",
    "1mo": "1d",
    "6mo": "1d",
    "1y": "1d",
    "5y": "1wk",
}

# On associe une période à une intervalle de récupération de données
# Les périodes sont disponibles dans la documentation de yfinance

INTRADAY = {"1m"}

def get_history(symbol, period="1y"):
    if period not in PERIODS:
        raise ValueError(f"Période inconnue : {period}")

    symbol = symbol.upper().strip()
    interval = PERIODS[period]
    ticker = yf.Ticker(symbol)

    df = ticker.history(
        period=period,
        interval=interval
    )
    if df.empty:
        return None

    df = df.dropna(subset=["Close"])

    # Avec un point par heure, il faut afficher l'heure en plus de la date
    date_format = "%d/%m %H:%M" if interval in INTRADAY else "%Y-%m-%d"

    data = {
        "symbol": symbol,
        "labels": df.index.strftime(date_format).tolist(),
        "values": df["Close"].round(2).tolist()
    }

    # On transforme les données qu'on a récupérées sur yfinance en dictionnaire

    return data
