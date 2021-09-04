#pip install pandas-datareader

from datetime import datetime

import pandas_datareader.data as web

start = datetime(2019, 1, 1) # year, month, day
end = datetime(2019, 2, 1)

mortgage_30_2019 = web.DataReader('MORTGAGE30US', 'fred', start, end)

sap_data = web.DataReader('SP500', 'fred', start, end)

inflation_2019 = web.DataReader('CPALTT01USM657N', 'fred', start, end)

print(sap_data)
print(inflation_2019)

inflation_2019.to_csv('inflation_2019.csv')
