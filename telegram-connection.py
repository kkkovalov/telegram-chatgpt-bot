from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from time import sleep

from dotenv import load_dotenv
load_dotenv("/Users/kovalov/Desktop/telegram-chatgpt-bot/.env")

import os

telegram_token = os.environ['TELEGRAM_API_KEY']

bot = Bot(token=telegram_token)

dp = Dispatcher(bot)

# store the given answer
answers = [] 


executor.start_polling(dp)

option_ask = KeyboardButton('Ask ChatGPT a question or help')
option_end = KeyboardButton('Exit the bot')
options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(option_ask).add(option_end)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Hello and welcome!\n Feel free to ask me a question at any time.', reply_markup=options_kb)
    

@dp.message_handler(regexp='Ask ChatGPT a question or help')
async def ask_gpt(message: types.Message):
    answers.append(message.text)
    await message.answer('')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('This a Telegram version of ChatGPT used to make interactions with AI easier and more flexible.')
    
