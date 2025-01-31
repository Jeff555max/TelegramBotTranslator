import asyncio  # Для работы с асинхронными функциями
from aiogram import Bot, Dispatcher, F  # Bot отвечает за взаимодействие с Telegram bot API
# Dispatcher управляет обработкой входящих сообщений и команд.
# Используем специальный класс F, который позволяет прописывать условия
# на получение сообщения
from aiogram.filters import Command, CommandStart  # Отслеживаем команду start и другие команды в Telegram-боте
# Для обработки команд импортируем нужные фильтры и типы сообщений:

from aiogram.types import Message  # Импортируем нужные типы сообщений
from config import TOKEN  # из файла config импортируем токен в основной файл
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

# (Handler) — это функция, выполняющая определенное действие в ответ на событие.
# Прописываем хендлер для обработки фото и варианты ответов:

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

# Прописываем хендлер для обработки текстового вопроса и вариант ответа
@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer(
        'Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')


# Создадим декоратор для обработки команды /help (пишем без слеш / )

@dp.message(Command('help'))  # (Handler) — это функция, выполняющая определенное действие в ответ на событие.
async def help(message: Message):  # Прописываем асинхронную функцию help, которая отправляет список команд бота
    await message.answer('Этот бот умеет выполнять команды:\n /start\n /help')  # \n  -для переноса на следующую строку


# Создадим декоратор для обработки команды /start

@dp.message(CommandStart())  # Тем самым мы будем брать сообщение (Message) и будем искать именно команду Start.
async def start(
        message: Message):  # При нахождении команды Start будет срабатывать функция, для которой прописан этот декоратор.
    await message.answer(
        "Хеви Метал, Бамбини!")  # Также через await мы прописали ответное действие: приветственное сообщение.


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
