import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from config import TOKEN  # импортируем токен из файла config
from gtts import gTTS  # Google TTS для озвучки текста
from googletrans import Translator  # Библиотека для перевода текста

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

# Проверяем и создаем папку, если её нет
if not os.path.exists("jpg"):
    os.makedirs("jpg")

if not os.path.exists("audio"):
    os.makedirs("audio")

# Хендлер для сохранения фото
@dp.message(F.photo)
async def react_photo(message: Message):
    try:
        photo_path = f'jpg/{message.photo[-1].file_id}.jpg'
        await bot.download(message.photo[-1], destination=photo_path)
        await message.answer("✅ Фото успешно сохранено!")
    except Exception as e:
        await message.answer(f"⚠️ Ошибка при сохранении фото: {e}")

# Хендлер для удаления всех фото по запросу
@dp.message(Command("delete_photo"))
async def delete_photo(message: Message):
    try:
        if not os.path.exists("jpg") or not os.listdir("jpg"):
            await message.answer("❌ Нет сохранённых фото для удаления.")
            return

        for file in os.listdir("jpg"):
            os.remove(f"jpg/{file}")

        await message.answer("✅ Все фото успешно удалены!")
    except Exception as e:
        await message.answer(f"⚠️ Ошибка при удалении фото: {e}")

# Хендлер для перевода текста и отправки голосового сообщения
@dp.message(F.text)
async def translate_text(message: Message):
    try:
        original_text = message.text
        translated_text = translator.translate(original_text, dest='en').text  # Переводим текст на английский

        # Сохраняем аудиофайл с переводом
        audio_path = "audio/translated.ogg"
        tts = gTTS(translated_text, lang="en")
        tts.save(audio_path)

        # Отправляем текст перевода
        await message.answer(f"🔠 Перевод: {translated_text}")

        # Отправляем голосовое сообщение
        voice_file = FSInputFile(audio_path)
        await bot.send_voice(message.chat.id, voice=voice_file)

    except Exception as e:
        await message.answer(f"⚠️ Ошибка перевода: {e}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
