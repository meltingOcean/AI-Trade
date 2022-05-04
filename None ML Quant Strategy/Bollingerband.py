import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import sys


def bollinger_band(price_df, n, sigma):
    bollinger_band = price_df.copy()
    bollinger_band['center'] = price_df['Close'].rolling(window=n).mean()    # center moving average
    bollinger_band['ub'] = bollinger_band['center'] + sigma*price_df['Close'].rolling(window=n).std()    # upper band
    bollinger_band['lb'] = bollinger_band['center'] - sigma*price_df['Close'].rolling(window=n).std()    # lower band
    return bollinger_band


def create_trade_book(sample):
    book = sample[['Close']].copy()
    book['trade'] = ''
    return book


def tradings(sample, book):
    for i in sample.index:
        if sample.loc[i, 'Close'] > sample.loc[i, 'ub']:
            book.loc[i, 'trade'] = ''
        elif sample.loc[i, 'lb'] > sample.loc[i, 'Close']:
            if book.shift(1).loc[i, 'trade'] == 'buy':
                book.loc[i, 'trade'] = 'buy'
            else:
                book.loc[i, 'trade'] = 'buy'
        elif sample.loc[i, 'ub'] >= sample.loc[i, 'Close'] and sample.loc[i, 'Close'] >= sample.loc[i, 'lb']:
            if book.shift(1).loc[i, 'trade'] == 'buy':
                book.loc[i, 'trade'] = 'buy'
            else:
                book.loc[i, 'trade'] = ''
    return(book)


def returns(book):
    # long only
    rtn = 1.0
    book['return'] = 1
    buy = 0.0
    sell = 0.0
    for i in book.index:
        if book.loc[i, 'trade'] == 'buy' and book.shift(1).loc[i, 'trade'] == '':
            buy = book.loc[i, 'Close']
            print('진입일 : ', i, 'long 진입가격 : ', buy)
        elif book.loc[i, 'trade'] == '' and book.shift(1).loc[i, 'trade'] == 'buy':
            sell = book.loc[i, 'Close']
            rtn = (sell - buy) / buy + 1
            book.loc[i, 'return'] = rtn
            print('청산일 : ', i, 'long 진입가격 : ', sell, ' | return:', round(rtn, 4))

        if book.loc[i, 'trade'] == '':
            buy = 0.0
            sell = 0.0

        acc_rtn = 1.0
    for i in book.index:
        rtn = book.loc[i, 'return']
        acc_rtn = acc_rtn * rtn
        book.loc[i, 'acc return'] = acc_rtn

    print('Accumulated return :', round(acc_rtn, 4))
    return(round(acc_rtn, 4))


n = 20        # size of window
sigma = 2  # number multiplied with sigma
base_date = '2018-02-01'

dataframe = fdr.DataReader(sys.argv[1], sys.argv[2])     # Index is already 'Date'
price_df = dataframe.loc[:, ['Close']].copy()    # Extract 'Close' column
bollinger = bollinger_band(price_df, n, sigma)
sample = bollinger.loc[base_date:]

book = create_trade_book(sample)
book = tradings(sample, book)
print(book.tail(50))
print(returns(book))
