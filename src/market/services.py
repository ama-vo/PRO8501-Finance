import yfinance as yf

PERIODS = {
    "7d": "1d",   
    "1mo": "5d",
    "6mo": "1d",
    "1y": "1d",
    "5y": "1mo"
}

# On associe une période à une intervalle de récupération de données
# Les périodes sont disponibles dans la documentation de yfinance

def get_history(symbol, period="1y"):
    symbol = symbol.upper().strip()
    ticker = yf.Ticker(symbol)

    df = ticker.history(
        period=period,
        interval=PERIODS[period]
    )
    if df.empty:   
       return None

    data = {
        "symbol": symbol,
        "labels": df.index.strftime("%Y-%m-%d").tolist(),
        "values": df["Close"].round(2).tolist()
    }

# On transforme les données qu'on a récupéré sur yfinance en dictionnaire

    return data
