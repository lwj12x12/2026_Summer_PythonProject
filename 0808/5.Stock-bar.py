import yfinance
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
code = '0050.TW'

result = yfinance.download(code,period='10d')

result.columns = result.columns.get_level_values(0)

plt.bar(result.index,result['Volume'])

plt.show()