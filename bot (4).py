import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types , filters
import config
import requests
from datetime import  datetime
from subs_class import Subs
from crypto_class import Crypto

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Configure logging

logging.basicConfig(level=logging.INFO)

#initialize the bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
fiatg = 'USD'
db_users = Subs('sqlite.db')
db_crypto = Crypto('sqlite.db',fiatg)

@dp.message_handler(commands=['start'])
async def step_one(message: types.Message):
    
    #This handler will be called when user sends `/start`  command
    
    
    await message.answer("""Hello, My name is CryptoWatch

You can get the latest cryptocurrency exchange rate, just type /start to begin.

You can also subscribe to a particular crypto price (get a trade signal), for example: “23000 < BTC” (number > or < Ticker).

 I will remind you when the price reaches the set value.

Subscribe to as much as you want, but do it wisely

/unsubscribe to stop the reminder
    """)
 

    rub = KeyboardButton('RUB')

    usd = KeyboardButton('USD')

    eur = KeyboardButton('EUR')

    cny = KeyboardButton('CNY')

    keyboard_fiat = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)

    keyboard_fiat.row(rub, usd).row(eur, cny)

    await message.answer('Choose fiat currency for comparison', reply_markup=keyboard_fiat)

    # unsubscribe handler
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    db_users.remove_subscriptions(int(message.from_user.id))
    await message.answer('You have successfully unsubscribed')

# catch subscribtions

@dp.message_handler(regexp=r'[0-9]+\s[>|<|=]\s[A-Z]+')
async def subscribe(message : types.Message):
    arr = message.text.split()
    cost = arr[0]
    more = arr[1]
    crypto = arr[2]
    user_id = message.from_user.id
    db_users.add_subscriber(user_id, crypto, more , cost)
    await message.answer('You have successfully subscribed')    
        
# handle with choosen fiat
@dp.message_handler(regexp='[A-Z]{3}')
async def step_two(message: types.Message):
   fiat = message.text
   db_crypto = Crypto('sqlite.db', fiat)
   courses_arr = db_crypto.get_courses(fiat) 
   answer = f"""
   Bitcoin {courses_arr[0]}\n
   Litecoin {courses_arr[1]}\n
   Dash {courses_arr[2]}\n
   Ethereum {courses_arr[3]}\n
   Ethereum Classic {courses_arr[4]}\n
   Neo {courses_arr[5]}\n
   IOTA {courses_arr[6]}\n
   Bitcoin Cash {courses_arr[7]}"""
   await message.answer(answer)

# loop

async def schudled():
        db_crypto.update_info()
        messages = db_users.subs_messages()
        for mes in messages:
            user_id = mes[0]
            text = mes[1]
            await bot.send_message(user_id , text)

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(12600, repeat, coro, loop)


 
# Starting long polling
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(12600, repeat, schudled, loop)
    executor.start_polling(dp, skip_updates=True, loop=loop)

