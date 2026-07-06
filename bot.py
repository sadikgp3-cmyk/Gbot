import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

# আপনার বটের টোকেনটি সরাসরি এখানে দিন অথবা এনভায়রনমেন্ট ভেরিয়েবল ব্যবহার করুন
API_TOKEN = '8420533816:AAFOH0l74RYPtJnHG12FBLPQfAzsk1xao6Y' 

# লগিং সেটআপ (এরর দেখার জন্য)
logging.basicConfig(level=logging.INFO)

# বট এবং ডিসপ্যাচার ইনিশিয়ালাইজ করা
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# মেইন মেনু বাটন
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("☎️ Get Number"), types.KeyboardButton("🌍 Available Country"))
    markup.row(types.KeyboardButton("📊 Status"), types.KeyboardButton("💰 Balance"))
    markup.row(types.KeyboardButton("😎 Withdraw"), types.KeyboardButton("🟢 Live Traffic"))
    return markup

# /start কমান্ড
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        f"❤️ Welcome {message.from_user.first_name}! 🎆\n\n💬 Main Menu\n\nPlease select an option below:",
        reply_markup=get_main_menu()
    )

# Get Number বাটন হ্যান্ডলার
@dp.message_handler(lambda message: message.text == "☎️ Get Number")
async def get_number_handler(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("FACEBOOK"), types.KeyboardButton("TIKTOK"))
    markup.add(types.KeyboardButton("⬅️ Back to Menu"))
    await message.answer("📶 Select a service: ⬇️", reply_markup=markup)

# Back to menu হ্যান্ডলার
@dp.message_handler(lambda message: message.text == "⬅️ Back to Menu")
async def back_handler(message: types.Message):
    await message.answer("🏠 Main Menu:", reply_markup=get_main_menu())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
