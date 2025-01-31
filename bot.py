import asyncio
import aiohttp
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import TOKEN  # из файла config импортируем токен в основной файл

API_KEY = "10be1f2ab5733726712558cedc95325e"
DEFAULT_CITY = "Tyumen"
INTERVALS = ["08:00", "14:00", "20:00"]
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    temp = data['main']['temp']
                    weather_desc = data['weather'][0]['description']
                    return f"Погода в  {city}: {temp}°C, {weather_desc}"
                else:
                    return f"Error {response.status}: City not found."
        except aiohttp.ClientError as e:
            return f"Weather API error: {e}"

async def send_weather():
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in INTERVALS:
            weather_report = await get_weather(DEFAULT_CITY)
            await bot.send_message(chat_id=CHAT_ID, text=weather_report)
            await asyncio.sleep(60)  # Ожидание, чтобы не спамить
        await asyncio.sleep(30)  # Проверяем каждую 30 секунд

@dp.message(Command("weather"))
async def weather_command(message: Message):
    city = message.text.split(" ", 1)
    if len(city) > 1:
        weather_report = await get_weather(city[1])
    else:
        weather_report = await get_weather(DEFAULT_CITY)
    await message.answer(weather_report)

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer('This bot can provide weather updates: \n /start \n /help \n /weather [city]')

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Hello! Use /weather [city] to get the current forecast.')

async def main():
    asyncio.create_task(send_weather())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
