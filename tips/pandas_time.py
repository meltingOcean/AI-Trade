
# | Concept      | Scalar class | Array class    | Data type
#  --------------------------------------------------------------------
# | Data Times   | Timestamp    | DatetimeIndex  | datetime64[ns]
# |              |              |                | or datetime[ns, tz]
# | Time deltas  | Timedelta    | TimedeltaIndex | timedelta[ns]
# | Time spans   | Period       | PeriodIndex    | period[freq]
# | Date offsets | DateOffset   | None           | None

# pandas library follows numpy's datetime64 type.
# Please copy and paste on python interpreter when you study these codes.


import pandas as pd

# Usage of Timestamp class
pd.Timestamp(1500.2351, unit='D')     # ISO 8601 times, YYYY-MM-DD hh:mm:ss
pd.Timestamp('2021-1-1 12')           # generate Timestamp object
pd.to_datetime('2021-1-1 12')

pd.to_datetime(['2020-1-1', '2021-1-2'])  # Genetate DatetimeIndex object
pd.date_range('2020-01', '2021-02')       # data type = datetime64[ns]

pd.Period('2021-01')                      # Time spans is 'period' of time.
pd.Period('2021-08', freq='D')            # 'freq' is frequency of dates.
pd.period_range('2021-01', '2021-02', freq='D')

A_period = pd.Period('2021-01')
A_period.start_time                       # Start time of 'A_period'
A_period.end_time                         # End time of 'A_period'

# Some kinds of argument 'freq'
# B    Business day
# W    Weekly
# M    Month
# More info
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html











