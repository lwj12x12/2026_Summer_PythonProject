import yfinance
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']

# code = ['0050.TW','0056.TW']

# code = input('請輸入台股代碼：')

code = '2330.TW'

result = yfinance.download(code, period='6mo')
# result = yfinance.download(code, start='2026-01-01', end='2026-08-07')

# print(result)
plt.title('2330走勢圖')
plt.plot(result.index, result['High'], label='最高價', color='red')
plt.plot(result.index, result['Low'], label='最低價', color='green')
plt.plot(result.index, result['Close'], label='收盤價', color='blue')

plt.legend()

plt.show()