from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import os

bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪 Ножи', '🥊 Перчатки', '🔫 Снайперские винтовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer('Выберите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='🔪 Ножи'))
async def get_discount_knives(message: types.Message):
  await message.answer('Please waiting...')

    
def main():
    executor.start_polling(dp)
    
    
if __name__ == '__main__':
    main()