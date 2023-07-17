from aiogram import Dispatcher, executor, Bot
from aiogram.types import Message
bot = Bot('6174917873:AAGaA83FzbFFzS12ndJtz5BOCntCnC3VZ40')
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f'Xsuh kelibsiz {message.from_user.full_name}')


executor.start_polling(dp, skip_updates=True)