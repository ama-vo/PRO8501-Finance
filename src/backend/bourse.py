import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

data = yf.download(
    tickers,
    period="1d",
    interval="1m",
    progress=False
)

fig, axes = plt.subplots(
    len(tickers),
    1,
    figsize=(12, 10),
    sharex=True
)

for i, ticker in enumerate(tickers):
    axes[i].plot(
        data.index,
        data["Close"][ticker]
    )

    axes[i].set_title(ticker)
    axes[i].set_ylabel("Prix ($)")
    axes[i].grid(True)

axes[-1].set_xlabel("Heure")

plt.tight_layout()
plt.show()