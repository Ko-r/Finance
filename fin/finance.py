import pandas as pd 
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime 

plt.style.use('seaborn')

msft = yf.Ticker('msft')
stockinfo = msft.info

print(msft.info)
print(msft.recommendations) 
print(msft.splits)
print(msft.institutional_holders)
print(type(msft.dividends))

df = msft.dividends

print(df)

data = df.resample('Y').sum()
data = data.reset_index()
data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'], data ['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title('Dividen Histroy')
plt.xlim(2002,2020)
plt.show()






