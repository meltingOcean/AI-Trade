# This file shows usage of important functions in pandas.
# These functions are useful to analysis data.
# Use csv file saved your local directory.

import pandas as pd

path = ''    # data file path
dataframe = pd.read_csv(path, index_col='Date', parse_dates=['Date'])

# pct_change() function
# calculate percentage change on period
# default periods is 1
dataframe['pct_change'] = dataframe['Close'].pct_change(periods=1)
print(dataframe)
