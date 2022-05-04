import pandas as pd
import numpy as np
import datetime
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

base_date = '2021-02-01'

dataframe = fdr.DataReader('005930', '2018')     # Index is already 'Date'
print(dataframe.head())