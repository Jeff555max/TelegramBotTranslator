import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from config import TOKEN  # импортируем токен из файла config
from gtts import gTTS  # Google TTS для озвучки текста
from googletrans import Translator  # Библиотека для перевода текста

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

# Создание каталога для аудиофайлов, если его нет
if not os.path.exists("audio"):
    os.makedirs("audio")

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