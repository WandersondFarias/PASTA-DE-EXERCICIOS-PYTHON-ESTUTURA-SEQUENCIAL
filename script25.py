import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker = 'AAPL'
data = yf.download(ticker, start='2019-01-01', end='2024-01-01')
plt.figure(figsize=(10, 6))
plt.plot(data['Adj Close'], label='Adj Close')
plt.title(f'Histórico de Preços para {ticker}')
plt.xlabel('Data')
plt.ylabel('Preço (USD)')
plt.legend()
plt.grid(True)
plt.show()
