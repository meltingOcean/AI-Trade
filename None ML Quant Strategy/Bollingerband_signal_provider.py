import pandas as pd
import FinanceDataReader as fdr
import sys


def bollinger_band(price_df, n, sigma):
    bollinger_band = price_df.copy()
    bollinger_band['center'] = price_df['Close'].rolling(window=n).mean()    # center moving average
    bollinger_band['ub'] = bollinger_band['center'] + sigma*price_df['Close'].rolling(window=n).std()    # upper band
    bollinger_band['lb'] = bollinger_band['center'] - sigma*price_df['Close'].rolling(window=n).std()    # lower band
    return bollinger_band

def create_trade_book(sample):
    book = sample[['Close']].copy()
    book['buy_signal_score'] = 0.0
    book['sell_signal_score'] = 0.0
    return book

def signal_provider(sample, book):
    for i in sample.index[1:]:
        book.loc[i, 'buy_signal_score'] = (sample.loc[i, 'center'] - sample.loc[i, 'Close'])/(sample.loc[i, 'ub'] - sample.loc[i, 'lb'])
        book.loc[i, 'sell_signal_score'] = (sample.loc[i, 'Close'] - sample.loc[i, 'center'])/(sample.loc[i, 'ub'] - sample.loc[i, 'lb'])
    return(book)


stocks = pd.read_csv('./stock_codes.csv', index_col='code')


for stock in stocks.index:

    dataframe = fdr.DataReader(stock[1:], '2021')     # Index is already 'Date'
    # argv[1] -> Stock Code

    n = 20        # size of window
    sigma = 2     # number multiplied with sigma
    base_date = '2021-02-01' # Date started trade

    price_df = dataframe.loc[:, ['Close']].copy()    # Extract 'Close' column, 'fdr' offer Adjusted Close as 'Close'
    bollinger = bollinger_band(price_df, n, sigma)
    sample = bollinger.loc[base_date:]

    book = create_trade_book(sample)
    book = signal_provider(sample, book)
    print(stocks.loc[stock, 'label'])
    print('Last Date: ',book.index[-1].strftime('%Y-%m-%d'))
    print('buy_signal_score: ', book.loc[book.index[-1], 'buy_signal_score'])
    print('sell_signal_score: ', book.loc[book.index[-1], 'sell_signal_score'])
