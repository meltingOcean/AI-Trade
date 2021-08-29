import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import tools.DataFrame_preprocess
# import FinanceDataReader as fdr


pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_rows', None)


# Using data from csv file
path = '/workspace/AI-Trade_/datas/AAPL.csv'
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])

# Using data from FinanceDataReader
# fdr.DataReader(Stock code, time spans)
# dataframe = fdr.DataReader('293490', '2020')

# When using option 'inplace', original dataframe is modified.
# Filling missing value(NaN, inf, -inf)

dataframe['daily_return'] = dataframe['Adj Close'].pct_change()

# replace infinity value to null value.
dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
dataframe.fillna(method='pad', inplace=True)
dataframe.fillna(method='bfill', inplace=True)

# DataFrame_preprocess.del_NaN_padbfill(dataframe)
# ^same function with above three lines

# print rows that have NaN or infinity value least 1
print(dataframe[dataframe.isin([np.nan, np.inf, -np.inf]).any(1)])

# dataframe.fillna(method='pad')  # forward filling
# dataframe.fillna(method='bfill') # backward filling


print(dataframe.head())

price_dataframe = dataframe.loc[:, ['Adj Close']].copy()
return_dataframe = dataframe.loc[:, ['daily_return']].copy()

# print(price_dataframe)
price_dataframe.plot(figsize=(16, 9), title='Adj Close')
plt.savefig('./plots/Adj_Close.png')

# print(return_dataframe)
return_dataframe.plot(figsize=(16, 9), title='return')
plt.savefig('./plots/return.png')






