import asyncio  # Для работы с асинхронными функциями
from aiogram import Bot, Dispatcher       # Bot отвечает за взаимодействие с Telegram bot API
                                          # Dispatcher управляет обработкой входящих сообщений и команд.

from aiogram.filters import CommandStart  # Отслеживаем команду start в Telegram-боте
                                          # Для обработки команд импортируем нужные фильтры и типы сообщений:

from aiogram.types import Message         # Импортируем нужные типы сообщений

bot = Bot(token='')
dp = Dispatcher()


async def main():  # Создадим асинхронную функцию main, которая будет запускать наш бот
    await dp.start_polling()

# async def main(). Это асинхронная функция main, которая будет запускаться и работать одновременно
# со всем остальным. await здесь — это действие, которое происходит с Telegram-ботом, и в нашем случае будет
# запускаться действие dp.start_polling: в этом случае программа будет отправлять запрос в Telegram, проверяя,
# есть ли входящие сообщения и произошедшие события. Если события есть, программа их “отлавливает”.
# В отсутствие событий функция продолжает отправлять запросы и ждет, когда событие произойдет,
# чтобы с этим можно было начать работать.

if __name__ == "__main__":
    asyncio.run(main())  # Мы пишем здесь не просто run(main), потому что функция здесь асинхронная,
    # ее нужно запускать определенным образом, указывая при этом, какую именно функцию мы хотим запустить.

# Создадим декоратор для обработки команды /start

@dp.message(CommandStart())  # Тем самым мы будем брать сообщение (Message) и будем искать именно команду Start.
async def start(message: Message):  # При нахождении команды Start будет срабатывать функция, для которой прописан этот декоратор.
    await message.answer("Хеви метал, бамбини, я бот!") # Также через await мы прописали ответное действие: приветственное сообщение.