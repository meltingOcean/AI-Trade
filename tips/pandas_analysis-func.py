# This code shows usage of important functions in pandas.
# These functions are useful to analysis data.
# Use csv file saved your local directory.

import pandas as pd

path = '/workspace/AI-Trade_/datas/AAPL.csv'    # data file path
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])

# pct_change() function
# calculate percentage change on period
# default periods is 1
dataframe['pct_change'] = dataframe['Close'].pct_change(periods=1)
print(dataframe)

# diff() function
# calcuate difference between on period
# default periods is 1

dataframe['close_diff'] = dataframe['Close'].diff(periods=1)
print(dataframe)

# rolling() function
# generate mean, max, min value in window size

dataframe['MovingAverage'] = dataframe['Close'].rolling(window=4).mean()
dataframe['Maximum'] = dataframe['Close'].rolling(window=4).max()
dataframe['Minimum'] = dataframe['Close'].rolling(window=4).min()
print(dataframe)
