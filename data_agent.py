import yfinance as yf
from indicators import add_indicators

def get_stock_data(ticker="RELIANCE.NS"):
    data = yf.download(ticker, period="1y", interval="1d")
    return data

data = get_stock_data()
data = add_indicators(data)

print(data[['Close','MA50','MA200']].tail())