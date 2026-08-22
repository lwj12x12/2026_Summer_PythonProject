import yfinance
import matplotlib.pyplot as plt
from fontTools.merge import layout

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
code = '0050.TW'

result = yfinance.download(code,period='1mo')
result.columns = result.columns.get_level_values(0)
#layout = plt.subplots(2,1)
fig,ax = plt.subplots(2,1)

ax[0].plot(result.index, result['Open'],color='blue')
ax[0].plot(result.index, result['Close'],color='green')
ax[1].bar(result.index, result['Volume'],color='red')

ax[0].set_title('0050走勢圖')
ax[1].set_title('成交量')

plt.show()