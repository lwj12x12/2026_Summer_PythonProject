import yfinance
import mplfinance as mpl
import matplotlib.pyplot as plt

code = '0050.TW'
result = yfinance.download(code, period='3mo', auto_adjust=False)
result.columns = result.columns.get_level_values(0)
print(result.columns)
result.columns = result.columns.get_level_values(0)
print(result.columns)

market_color = mpl.make_marketcolors(
    up='red',
    down='green',
    inherit=True
)

style = mpl.make_mpf_style(
    marketcolors=market_color,
)


mpl.plot(result, type='candle', style=style,volume=True,mav=5)