from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from logic import *
from config import *

bot = TeleBot(API_TOKEN)

def gen_markup(id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Получить!", callback_data=id))
    return markup

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер проектов
Помогу тебе сохранить твои проекты и информацию о них!) 
""")

@bot.message_handler(commands=['select_star'])
def search(message):
    user_request = bot.send_message(message.chat.id, "Введите название звезды:")
    bot.register_next_step_handler(message, user_request)

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()