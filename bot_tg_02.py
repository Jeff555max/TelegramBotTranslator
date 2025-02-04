import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

SAVE_DIR = "jpg"  # Папка для сохранения фото

# Обработчик фото
@dp.message(F.photo)
async def react_photo(message: Message):
    try:
        file_id = message.photo[-1].file_id  # Получаем ID самого большого фото
        file = await bot.get_file(file_id)  # Запрашиваем путь файла у Telegram
        file_path = file.file_path

        os.makedirs(SAVE_DIR, exist_ok=True)  # Создаём папку, если её нет
        save_path = os.path.join(SAVE_DIR, f"{file_id}.jpg")

        await bot.download_file(file_path, save_path)  # Скачиваем фото

        # Укорачиваем callback_data (берём только первые 10 символов ID)
        short_id = file_id[:10]

        # Создаём клавиатуру с кнопками "Удалить" и "Оставить"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🗑 Удалить", callback_data=f"del_{short_id}")],
            [InlineKeyboardButton(text="✅ Оставить", callback_data=f"keep_{short_id}")]
        ])

        await message.answer(f"📸 Фото сохранено!\nУдалить?", reply_markup=keyboard)

    except Exception as e:
        await message.answer(f"⚠️ Ошибка при сохранении фото: {e}")

# Обработчик удаления фото
@dp.callback_query(F.data.startswith("del_"))
async def delete_photo_callback(query: CallbackQuery):
    short_id = query.data.split("_")[1]  # Достаём короткий ID
    file_path = None

    # Поиск полного имени файла по укороченному ID
    for filename in os.listdir(SAVE_DIR):
        if filename.startswith(short_id):
            file_path = os.path.join(SAVE_DIR, filename)
            break

    if file_path and os.path.exists(file_path):  # Проверяем, найден ли файл
        os.remove(file_path)  # Удаляем файл
        await query.message.edit_text(f"✅ Фото удалено.")
    else:
        await query.message.edit_text(f"⚠️ Фото не найдено!")

# Обработчик оставления фото
@dp.callback_query(F.data.startswith("keep_"))
async def keep_photo_callback(query: CallbackQuery):
    await query.message.edit_text(f"✅ Фото сохранено.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
