#import yfinance

#code = '2330.TW' #台灣股市記得後面接.TW、日經股市接.T、美國股市不須接

#stock = yfinance.download(code,period='1d')  #1D=一天、1mo=一月、1y=一年

#print(stock)

import yfinance

code = input('請輸入台股代碼：')

result = yfinance.download(f'{code}.TW', period='1y')

print(result)