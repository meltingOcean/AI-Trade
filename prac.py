
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
pd.Timestamp(1239.1238934, unit='D')
pd.Timestamp('2021-1-1')
pd.to_datetime('2021-1-1 12')
pd.to_datetime(['2020-1-1', '2021-1-2'])
pd.date_range('')