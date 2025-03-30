### TelegramBotTranslator
Это бот для Telegram, который переводит текст на английский язык и озвучивает его. Для работы бота используются следующие библиотеки:

aiogram — для работы с Telegram Bot API.

googletrans — для перевода текста.

gTTS — для синтеза речи (Text-to-Speech).

Функциональность

Перевод текста: Бот автоматически переводит полученные сообщения на английский язык.

Озвучка: Переведённый текст преобразуется в аудиосообщение.

Легкость использования: Простота установки и настройки для быстрого запуска.

Требования
Python 3.6 и выше

Установка

Клонируйте репозиторий:

git clone https://github.com/Jeff555max/TelegramBotTranslator.git

cd TelegramBotTranslator

Установите необходимые библиотеки:

Выполните следующие команды:


pip install aiogram
pip install googletrans==4.0.0-rc1 gtts

Либо установите зависимости через файл requirements.txt:

pip install -r requirements.txt

Настройка

Перед запуском бота необходимо настроить токен, полученный у BotFather.

Откройте файл config.py.

Замените значение переменной TOKEN на ваш настоящий токен.

Для запуска бота выполните команду:

python bot.py

После запуска, отправьте любое текстовое сообщение в Telegram. Бот ответит переводом сообщения на английский язык и аудиофайлом с озвученным текстом.

Лицензия

Проект распространяется под лицензией MIT License.



