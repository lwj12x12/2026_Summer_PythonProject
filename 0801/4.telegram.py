import bs4
import requests
import os #讀取資料夾
from dotenv import load_dotenv #毒環境檔
from telegram import Update #取得更新
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler, #處理命令
    MessageHandler, #回復訊息
    ContextTypes, #處裡訊息
    filters #過濾
) #設機器人

#讀取.env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

#取得RSS
def get_rss():
    url = 'https://www.twse.com.tw/rwd/zh/news/feed?type=rss'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    result =[]
    for item in items:
        title = item.find('title').text
        content = item.find('content:encoded').text
        result.append(title)
        print(title)
        print(content)
    return result

#處理 /start指令
async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "你好，我是 RSS小機器人！\n"
        "你可以傳送任何文字給我。"
    )
#處理greet
async def greet_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
      "HeLLO & BYE"
    )

#處理 /news1
async def news1_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        f'{get_rss()[0]}\n{get_rss()[1]}\n{get_rss()[2]}'

    )

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

    # 加入 /greet指令處理器
    application.add_handler(
        CommandHandler("greet", greet_command)
    )

    # 加入 /news指令處理器
    application.add_handler(
        CommandHandler("news1", news1_command)
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