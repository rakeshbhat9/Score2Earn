import pandas as pd
import quandl
import datetime
from datetime import datetime as dt


def rate():
    usdinr = pd.DataFrame(quandl.get("CUR/INR", authtoken="ENTER YOUR TOKEN HERE"))
    today = dt.today()
    y = today - datetime.timedelta(1)
    yesterday = y.strftime('%Y-%m-%d')
    r = usdinr.ix[yesterday][0]

 #   print r
    return r
