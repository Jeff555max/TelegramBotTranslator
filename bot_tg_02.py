import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from config import TOKEN  # из файла config импортируем токен в основной файл
from gtts import gTTS  # сделать озвучку Google TTS
import os

