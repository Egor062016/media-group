from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token="5866449991:AAGPn8v7gem8lCmfVAibW3vAjaaAW1mGG3c")
dp = Dispatcher(bot)

async def say_thanks(user: types.User):
    await bot.send_message(user.id, "Спасибо, поехали дальше...")


async def photo_handler(message: types.Message):
    await say_thanks(message.from_user)
    photo = message.photo.pop()
    
    await photo.download(f'download/{str(random.randint(1, 99))}.jpg')

dp.register_message_handler(photo_handler, content_types=['photo'])
executor.start_polling(dp, skip_updates=True)
