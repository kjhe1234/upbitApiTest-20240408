# pip install python-telegram-bot

import telegram
import asyncio

bot = telegram.Bot(token="6597392316:AAEoC_XnKgA3OUyc0_y44-tDQ8lZvWb6rqQ")
chat_id = "7052945803"

asyncio.run(bot.sendMessage(chat_id=chat_id, text="안녕하세요!! 파이썬 텔레그램 테스트!!"))
