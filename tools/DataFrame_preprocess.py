import numpy as np


def del_NaN_padbfill(dataframe):
    dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
    dataframe.fillna(method='pad', inplace=True)
    dataframe.fillna(method='bfill', inplace=True)


def del_NaN_bfillpad(dataframe):
    dataframe.replace([np.inf, -np.inf], np.nan, inplace=True)
    dataframe.fillna(method='bfill', inplace=True)
    dataframe.fillna(method='pad', inplace=True)
    