import pandas as pd
import numpy as np


path = '/workspace/AI-Trade_/datas/AAPL.csv'
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])
dataframe['Daily Return'] = dataframe['Adj Close'].pct_change()
dataframe['Cumul Return'] = (1 + dataframe['Daily Return']).cumprod()

# CAGR(Compound Anuual Growth Rate)

CAGR = dataframe.loc['2020-09-09', 'Cumul Return'] ** (252./len(dataframe.index)) - 1
print(CAGR)