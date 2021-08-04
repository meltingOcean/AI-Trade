
# | Concept      | Scalar class | Array class    | Data type
#  --------------------------------------------------------------------
# | Data Times   | Timestamp    | DatetimeIndex  | datetime64[ns]
# |              |              |                | or datetime[ns, tz]
# | Time deltas  | Timedelta    | TimedeltaIndex | timedelta[ns]
# | Time spans   | Period       | PeriodIndex    | period[freq]
# | Date offsets | DateOffset   | None           | None
import pandas as pd


# pandas follws numpy's datetime64 type
# Usage of Timestamp class
pd.Timestamp(1500.2351, unit='D')     # ISO 8601 times, YYYY-MM-DD hh:mm:ss
pd.Timestamp('2021-1-1 12')           # generate Timestamp object
pd.to_datetime('2021-1-1 12')

pd.to_datetime(['2020-1-1', '2021-1-2'])  # genetate DatetimeIndex object
pd.date_range('2020-01', '2021-02')       # data type = datetime65[ns]
