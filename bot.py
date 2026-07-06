import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

# টোকেন লোড করা (নিরাপত্তার জন্য)
load_dotenv()
API_TOKEN = os.getenv("8420533816:AAFOH0l74RYPtJnHG12FBLPQfAzsk1xao6Y")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# মেনু বাটন তৈরি
def get_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("☎️ Get Number"), KeyboardButton("🌍 Available Country"))
    markup.add(KeyboardButton("📊 Status"), KeyboardButton("💰 Balance"))
    markup.add(KeyboardButton("😎 Withdraw"), KeyboardButton("🟢 Live Traffic"))
    return markup

# /start কমান্ড
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"❤️ Welcome {message.from_user.first_name}! 🎆\n\n💬 Main Menu\n\n⬇️ Please select an option below:",
        reply_markup=get_main_menu()
    )

# Get Number হ্যান্ডলার
@dp.message_handler(lambda message: message.text == "☎️ Get Number")
async def get_number(message: types.Message):
    # সার্ভিস সিলেকশন বাটন
    service_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    service_markup.add(KeyboardButton("FACEBOOK"), KeyboardButton("TIKTOK"))
    await message.answer("📶 Select a service: ⬇️", reply_markup=service_markup)

# বটের রান টাইম
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
