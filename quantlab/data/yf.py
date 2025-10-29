import yfinance as yf
from datetime import date, timedelta

def priceData(stocks: list, length: int):
    data = yf.download(
        tickers = stocks,
        start = date.today() - timedelta(days = length),
        end = date.today(),
    )
    return data["Close"]