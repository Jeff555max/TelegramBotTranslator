import asyncio  # Для работы с асинхронными функциями
from aiogram import Bot, Dispatcher, F  # Bot отвечает за взаимодействие с Telegram bot API
# Dispatcher управляет обработкой входящих сообщений и команд.
# Используем специальный класс F, который позволяет прописывать условия
# на получение сообщения
from aiogram.filters import Command, CommandStart  # Отслеживаем команду start и другие команды в Telegram-боте
# Для обработки команд импортируем нужные фильтры и типы сообщений:

from aiogram.types import Message, FSInputFile # Импортируем нужные типы сообщений, для работы с файлами нужно импортировать класс FSInputFile
from config import TOKEN  # из файла config импортируем токен в основной файл
import random

from gtts import gTTS  # сделать озвучку Google TTS
import os

bot = Bot(token=TOKEN)
dp = Dispatcher()

# (Handler) — это функция, выполняющая определенное действие в ответ на событие.

@dp.message(Command('video')) # на команду пользователя /video будет отправляться видео и будет сообщение, что видео отправляется
async def video(message: Message):  # Мы создаем переменную video, в которой хранится объект класса FSInputFile.
    await bot.send_chat_action(message.chat.id, 'upload_video') # Уведомление о загрузке. Это уведомление покажет,
    # что бот загружает видео. Когда загрузка завершится, уведомление исчезнет
    video = FSInputFile('1ddb0b17.mp4')
# В скобках указываем путь к файлу. Если файл находится в одной папке с main.py, достаточно указать только его название.
# Если он находится в другой папке, перед названием нужно прописать полностью путь к файлу.
    await bot.send_video(message.chat.id, video)  # Теперь используем одну из двух команд для отправки видео:
    # message.answer_video или bot.send_video. Также указываем ID чата, откуда пришла команда, и переменную video.
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))# важно знать о голосовых сообщениях: формат MP3 здесь не поддерживается, для этого нужен формат OGG
async def voice(message: Message):
    voice = FSInputFile("sample.ogg")
    await message.answer_voice(voice) # можно использовать message.answer — в этом случае не нужно будет указывать chat.id.
    # или bot.send_voice(message.chat.id, voice)

@dp.message(Command('audio')) # на команду пользователя /audio будет отправляться аудио
async def audio(message: Message):
    audio = FSInputFile('1.MP3')
    await bot.send_audio(message.chat.id, audio) # Указываем ID чата, откуда пришла команда в тот чат отправится ответ -переменная audio


@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
    # Для отправки MP3 файла
    tts = gTTS(text=rand_tr, lang='ru')  # Создадим объект класса GoogleTTS. В круглых скобках при этом указываем
    # параметр text и задаем ему значение, какой именно текст нужно преобразовать в голос.
    # Этот текст хранится в переменной rand_tr. Также необходимо указать, на каком языке нам нужна озвучка,
    # так как по умолчанию это будет английский язык
    tts.save("training.mp3")  # Чтобы сохранить то, что мы создадим, нужно прописать специальную команду save,
    # указав при этом название файла, в который будут сохраняться эти данные
    audio = FSInputFile('training.mp3') # Далее эти данные нужно отправить. Для этого создаем переменную audio,
    # в круглых скобках прописываем название файла и отправляем
    await bot.send_audio(message.chat.id, audio) # — для этого мы используем await, а в круглых скобках указываем ****chat.id и
    # передаем аудио для отправки.
    os.remove("training.mp3") # Также прописываем remove, так как после отправки файл можно удалить

    # Для отправки OGG файла голосового сообщения
    tts = gTTS(text=rand_tr, lang='ru')  # Создадим объект класса GoogleTTS. В круглых скобках при этом указываем
    # параметр text и задаем ему значение, какой именно текст нужно преобразовать в голос.
    # Этот текст хранится в переменной rand_tr. Также необходимо указать, на каком языке нам нужна озвучка,
    # так как по умолчанию это будет английский язык
    tts.save("training.ogg")  # Чтобы сохранить то, что мы создадим, нужно прописать специальную команду save,
    # указав при этом название файла, в который будут сохраняться эти данные
    audio = FSInputFile('training.ogg')  # Далее эти данные нужно отправить. Для этого создаем переменную audio,
    # в круглых скобках прописываем название файла и отправляем
    await bot.send_audio(message.chat.id, audio)  # — для этого мы используем await, а в круглых скобках указываем ****chat.id и
    # передаем аудио для отправки.
    os.remove("training.ogg")  # Также прописываем remove, так как после отправки файл можно удалить


# Прописываем хендлер для обработки фото и варианты ответов:
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg') # Сначала указываем message.photo и
    # в квадратных скобках -1. Затем добавляем запятую и указываем атрибут destination, который равен строке 'tmp/'.
    # Это будет наша папка для хранения файлов. В фигурных скобках мы прописали message.photo[-1].file_id.
    # Это делается для того, чтобы у фотографий были уникальные имена. Таким образом, мы будем сохранять
    # все фотографии в папке tmp, и у каждой фотографии будет название, соответствующее её ID и расширение jpg.
    # Почему мы используем -1 в квадратных скобках? Когда мы отправляем фотографию, Telegram отправляет несколько ее копий
    # в разных размерах. Мы выбираем последнюю версию, так как она имеет максимальный доступный размер и наиболее удобна для нас.
    # Поэтому указываем -1, что означает последнюю версию изображения. И, наконец, мы указываем ID фотографии,
    # чтобы присвоить ей уникальное имя.

# Прописываем хендлер для обработки текстового вопроса и вариант ответа
@dp.message(F.text.lower() == "что такое ии?")
async def aitext(message: Message):
    await message.answer(
        'Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

# Также бот и сам может отправлять пользователям фотографии. Пропишем команду для этого. Фотографии можно
# отправлять по ссылкам — это самый простой вариант. Мы можем взять в Google несколько ссылок на фотографии и
# отправлять их, опять-таки, рандомно. Для этого копируем URL выбранных изображений и вставляем их в код.
# В конце ссылки обязательно должно быть указано расширение изображения.

@dp.message(Command("photo",prefix='&'))  # Добавляем обработчик команды /photo,
# Когда мы отправляем любую команду боту в Telegram, по умолчанию используется слэш перед командой. Но мы можем задать и свои префиксы
# с префиксом, например & пользователю надо будет писать &photo
async def photo(message: Message):
    photo_list = ["https://content.onliner.by/forum/5c4/a3b/397580/800x800/091bac2b9ea25d7551a41e0bde4726ec.jpg",]
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption="Это супер крутая картинка")

# Создадим декоратор для обработки команды /help (пишем без слеш / )

@dp.message(Command('help'))  # (Handler) — это функция, выполняющая определенное действие в ответ на событие.
async def help(message: Message):  # Прописываем асинхронную функцию help, которая отправляет список команд бота
    await message.answer('Этот бот умеет выполнять команды:\n /start\n /help\n /photo')  # \n  -для переноса на следующую строку


# Создадим декоратор для обработки команды /start

@dp.message(CommandStart())  # Тем самым мы будем брать сообщение (Message) и будем искать именно команду Start.
async def start(message: Message):  # При нахождении команды Start будет срабатывать функция, для которой прописан этот декоратор.
    await message.answer(f'Приветики, {message.from_user.full_name}')  # Также через await мы прописали ответное действие:
    # приветственное сообщение с именем first_name или полным именем full_name пользователя


# @dp.message() # обрабатывает любые сообщения, отвечает эхом (прописывают всегда в самом низу обработчик для всех команд и сообщений)
# async def start(message: Message):
    # await message.send_copy(chat_id=message.chat.id) # будет отправлять те же сообщения в чат откуда отправлено сообщение

@dp.message() # обрабатывает любые сообщения, в данном случае слово 'тест' (прописывают всегда в самом низу обработчик для всех команд и сообщений)
async def start(message: Message):
    if message.text.lower() == 'test':  # Отслеживание сообщений с помощью условного оператора
        await message.answer('Тестируем')  # Для отслеживания определенных сообщений с текстом можно также использовать условия.
        # Мы объявляем декоратор @dp.message(), который указывает, что функция будет обрабатывать сообщения.
        # Затем объявляем асинхронную функцию start, которая принимает параметр message типа Message.
        # Внутри функции проверяем, равно ли текст сообщения message.text строке 'test' с приведением к нижнему регистру (lower).
        # Это делается для того, чтобы условие срабатывало независимо от регистра введенного текста.
        # Пишем боту слово “test”, и он отвечает: “Тестируем”. Это еще один способ отслеживать текст.



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
