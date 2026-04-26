import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "GOOGL"]

for stock in stocks:
    df = yf.Ticker(stock).history(period="1mo")
    print(f"\n{stock}")
    print(df.head())
    df.to_csv(f"{stock}_ohlcv.csv")

print("Done!")
