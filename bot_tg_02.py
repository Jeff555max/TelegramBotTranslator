import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from config import TOKEN  # из файла config импортируем токен в основной файл
from gtts import gTTS  # сделать озвучку Google TTS
import os

# Прописываем хендлер для обработки фото и варианты ответов:
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'jpg/{message.photo[-1].file_id}.jpg') # Сначала указываем message.photo и
    # в квадратных скобках -1. Затем добавляем запятую и указываем атрибут destination, который равен строке 'tmp/'.
    # Это будет наша папка для хранения файлов. В фигурных скобках мы прописали message.photo[-1].file_id.
    # Это делается для того, чтобы у фотографий были уникальные имена. Таким образом, мы будем сохранять
    # все фотографии в папке tmp, и у каждой фотографии будет название, соответствующее её ID и расширение jpg.
    # Почему мы используем -1 в квадратных скобках? Когда мы отправляем фотографию, Telegram отправляет несколько ее копий
    # в разных размерах. Мы выбираем последнюю версию, так как она имеет максимальный доступный размер и наиболее удобна для нас.
    # Поэтому указываем -1, что означает последнюю версию изображения. И, наконец, мы указываем ID фотографии,
    # чтобы присвоить ей уникальное имя.
