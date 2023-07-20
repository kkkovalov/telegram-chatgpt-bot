import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F, html
from aiogram.filters.command import Command
from aiogram.filters import CommandObject, Text
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods.close import Close
from dotenv import load_dotenv

# Load local .env file info to os enviromentals
load_dotenv("/Users/kovalov/Desktop/telegram-chatgpt-bot/.env")

# Turn on logging for important messages
logging.basicConfig(level=logging.INFO)

# Bot object
telegram_token = os.environ['TELEGRAM_API_KEY']
bot = Bot(token=telegram_token, parse_mode='HTML')

# Dispatcher set up
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Store input data
user_prompt = ""

# 'Start' command handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Ask a question")],
        [types.KeyboardButton(text="Exit ChatGPT")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Make your choice!")
    await message.answer("Welcome to Telegram version of ChatGPT by kkkovallov. Please select you next action.", reply_markup=keyboard)

@dp.message(Text("Ask a question"))
async def ask_question(message: types.Message):
    global user_prompt
    user_prompt = ""
    await message.reply('Very well!\nEnter you question: ', reply_markup=types.ReplyKeyboardRemove())

@dp.message(Text('Exit ChatGPT'))
async def exit_bot(message: types.Message):
    await message.answer("Thank you for using ChatGPT!", reply_markup=types.ReplyKeyboardRemove())
    bot.close()

@dp.message()
async def handle_prompt(message: types.Message):
    global user_prompt
    if user_prompt == "":
        user_prompt = message.text
        await message.reply("Prompt saved!")
    else:
        kb = [
            [types.KeyboardButton(text="Ask a question")],
            [types.KeyboardButton(text="Exit ChatGPT")]
        ]
        await message.reply("I'm sorry, I don't understand. Please make your selection", reply_markup=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Make your choice!"))



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
        
if __name__ == "__main__":
    asyncio.run(main())