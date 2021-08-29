import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/workspace/AI-Trade_/datas/AAPL.csv'
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])
dataframe['Daily Return'] = dataframe['Adj Close'].pct_change()
dataframe['Cumul Return'] = (1 + dataframe['Daily Return']).cumprod()

base_date = '2020-09-10'
temp_df = dataframe.loc[base_date:, ['Cumul Return']] / dataframe.loc[base_date, ['Cumul Return']]
last_date = temp_df.index[-1]
print(temp_df.loc[last_date, 'Cumul Return'])
temp_df.plot(figsize=(16, 9))
plt.savefig('/workspace/AI-Trade_/plots/cumulreturn.png')
