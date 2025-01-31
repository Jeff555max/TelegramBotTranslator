import asyncio  # Для работы с асинхронными функциями
from aiogram import Bot, Dispatcher       # Bot отвечает за взаимодействие с Telegram bot API
                                          # Dispatcher управляет обработкой входящих сообщений и команд.

from aiogram.filters import Command, CommandStart  # Отслеживаем команду start и другие команды в Telegram-боте
                                          # Для обработки команд импортируем нужные фильтры и типы сообщений:

from aiogram.types import Message         # Импортируем нужные типы сообщений
from config import TOKEN  # из файла config импортируем токен в основной файл

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создадим декоратор для обработки команд

@dp.message(Command('help')) # (Handler) — это функция, выполняющая определенное действие в ответ на событие.
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n /start\n /help')  # \n  -для переноса на следующую строку

# Создадим декоратор для обработки команды /start

@dp.message(CommandStart())  # Тем самым мы будем брать сообщение (Message) и будем искать именно команду Start.
async def start(message: Message):  # При нахождении команды Start будет срабатывать функция, для которой прописан этот декоратор.
    await message.answer("Хеви Метал, Бамбини!") # Также через await мы прописали ответное действие: приветственное сообщение.

async def main():  # Создадим асинхронную функцию main, которая будет запускать наш бот
    await dp.start_polling(bot)

# async def main(). Это асинхронная функция main, которая будет запускаться и работать одновременно
# со всем остальным. await здесь — это действие, которое происходит с Telegram-ботом, и в нашем случае будет
# запускаться действие dp.start_polling: в этом случае программа будет отправлять запрос в Telegram, проверяя,
# есть ли входящие сообщения и произошедшие события. Если события есть, программа их “отлавливает”.
# В отсутствие событий функция продолжает отправлять запросы и ждет, когда событие произойдет,
# чтобы с этим можно было начать работать.

if __name__ == "__main__":
    asyncio.run(main())  # Мы пишем здесь не просто run(main), потому что функция здесь асинхронная,
    # ее нужно запускать определенным образом, указывая при этом, какую именно функцию мы хотим запустить.

