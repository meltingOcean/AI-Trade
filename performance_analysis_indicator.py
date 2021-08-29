import pandas as pd
import numpy as np


path = '/workspace/AI-Trade_/datas/AAPL.csv'
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])
dataframe['Daily Return'] = dataframe['Adj Close'].pct_change()
dataframe['Cumul Return'] = (1 + dataframe['Daily Return']).cumprod()

# CAGR(Compound Anuual Growth Rate)

CAGR = dataframe.loc['2021-08-06', 'Cumul Return'] ** (252./len(dataframe.index)) - 1
Sharpe = np.mean(dataframe['Daily Return']) / np.std(dataframe['Daily Return']) * np.sqrt(252.)
VOL = np.std(dataframe['Daily Return']) * np.sqrt(252.)
historical_max = dataframe['Adj Close'].cummax()
daily_drawdown = dataframe['Adj Close'] / historical_max - 1.0
historical_dd = daily_drawdown.cummin()
MDD = historical_dd.min()

print('CAGR : ', round(CAGR*100,2), '%')
print('Sharpe : ', round(Sharpe, 2))
print('VOL : ', round(VOL*100,2), '%')
print('MDD : ', round(-1*MDD*100,2), '%')
