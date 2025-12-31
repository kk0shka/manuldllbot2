import telebot
from telebot import types

# Вставь сюда свой токен от @BotFather
TOKEN = '8286452540:AAFhmtp5FrdIX634FalrhC39GhRxEjY9Ook'

bot = telebot.TeleBot(TOKEN)

# Ссылки
IMAGE_START = "https://cdn.discordapp.com/attachments/1422937523616878642/1455975831372562472/Untitled.png?ex=6956aea8&is=69555d28&hm=f5f2e5f44837ad4ebaabe0e823fe387f80f763bfceeeb3b9737ed7f30bf311fe&"
IMAGE_CHEATS = "https://cdn.discordapp.com/attachments/1422937523616878642/1455981318235226377/Untitl1ed.png?ex=6956b3c5&is=69556245&hm=a3909e2a57a8ea778bfa273e5521192c3ba700cd995358862f23288e1c807135&"
DOWNLOAD_URL = "https://github.com/amnyamchik/manulldllproject/raw/refs/heads/main/BootstrapperNew.exe"


# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопку "Читы"
    markup = types.InlineKeyboardMarkup()
    btn_cheats = types.InlineKeyboardButton(text="Читы", callback_data="open_cheats")
    markup.add(btn_cheats)

    caption_text = "привет, приветсвую тебя в моем тг боте с читами, анлокали и реворсили моя команда manulgang"

    # Отправляем первое фото
    try:
        bot.send_photo(message.chat.id, IMAGE_START, caption=caption_text, reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, f"{caption_text}\n\n(Ошибка загрузки фото, но кнопки работают)",
                         reply_markup=markup)
        print(f"Ошибка: {e}")


# Обработка нажатия на кнопку "Читы"
@bot.callback_query_handler(func=lambda call: call.data == "open_cheats")
def show_cheats(call):
    # Создаем кнопку-ссылку "Roblox Solara"
    markup = types.InlineKeyboardMarkup()
    btn_download = types.InlineKeyboardButton(text="Roblox Solara", url=DOWNLOAD_URL)
    markup.add(btn_download)

    # Отправляем второе фото
    try:
        bot.send_photo(call.message.chat.id, IMAGE_CHEATS, caption="Доступное ПО:", reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, "Доступное ПО (фото не загрузилось):", reply_markup=markup)
        print(f"Ошибка при нажатии кнопки: {e}")

    # Убираем состояние загрузки на кнопке
    bot.answer_callback_query(call.id)


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()