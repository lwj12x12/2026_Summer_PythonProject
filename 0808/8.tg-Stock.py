import os
import yfinance

from dotenv import load_dotenv
from telegram import Update,Bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import requests
import bs4
#########################################
# 讀取.env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
############################################

# 取得rss
def get_rss():
    url = 'https://www.twse.com.tw/rwd/zh/news/feed?type=rss'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    result = []
    for item in items:
        title = item.find('title').text
        content = item.find('content:encoded').text
        result.append({
            'title': title,
            'content': content
        })
        # print(title)
        # print(content)
    return result

# 取得股市資料
def get_stock(code):
    data = yfinance.download(f'{code}.TW', period='1d')
    return data

def get_stock_now(code):
    data = yfinance.Ticker(f'{code}.TW')
    return data.fast_info['lastPrice']
# 處理 /start 指令
async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "你好，我是 RSS激起人！\n"
        "你可以傳送任何文字給我。"
    )
#
async def stock_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if len(context.args) == 0:
        await update.message.reply_text('請輸入股票代碼，如 /stock 2330')
        return
    if len(context.args) == 2:
        await update.message.reply_text(
            f'現在股價為：{get_stock_now(context.args[0])}'
        )
        return
    data = get_stock(context.args[0])
    open = data['Open']
    high = data['High']
    low = data['Low']
    close = data['Close']
    volume = data['Volume']
    await update.message.reply_text(
        f'開盤價{open} \n'
        f'收盤價{close} \n'
        f'最高價{high} \n'
        f'最低價{low} \n'
        f'成交量{volume} \n'
    )

#################
async def greeting_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    for index,news in enumerate(get_rss()):
        await update.message.reply_text(
            f'{news['title']}'
            f'\n{news["content"]}'
        )
        if index == 10:
            break

######################################################
# 處理一般文字訊息
async def echo_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    # 取得使用者輸入的文字
    user_text = update.message.text

    print("使用者輸入：", user_text)

    # 將相同的文字回覆給使用者
    await update.message.reply_text(
        f"你說了：{user_text}"
    )

##############################################
# 主程式
def main():
    if not TELEGRAM_BOT_TOKEN:
        print("找不到TOKEN")
        print("請檢查.env")
        return

    # 建立Telegram Bot應用程式
    application = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    # 加入 /start指令處理器
    application.add_handler(
        CommandHandler("start", start_command)
    )
    # 加入 /stock指令處理器
    application.add_handler(
        CommandHandler("stock", stock_command)
    )
    # 加入 /greeting
    application.add_handler(
        CommandHandler("news1", greeting_command)
    )

    # 加入一般文字訊息處理器
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            echo_message
        )
    )

    print("Telegram Bot 已啟動")
    print("按下 Ctrl + C 可以停止程式")

    # 持續接收 Telegram 訊息
    application.run_polling()


if __name__ == "__main__":
    main()