
from constants import API_KEY
from constants import defaults_messages 
from constants import chat_id_dic
import telebot
from telebot.apihelper import ApiTelegramException
from HelperClasses import Verifier



bot = telebot.TeleBot(API_KEY)
verifier = Verifier(bot)
verifier.set_chat_id_dic(chat_id_dic)


@bot.message_handler(commands=['start'])
def send_start_msg(message):
    bot.send_message(message.chat.id,defaults_messages["start"],parse_mode='HTML')

    
@bot.message_handler(commands=['verify'])
def send_verification_result(message):
    if verifier.result(message.from_user.id) is True:
        bot.send_message(message.chat.id,defaults_messages["verified_msg"],parse_mode='HTML')
    else : 
        bot.send_message(message.chat.id,defaults_messages["verify_error"],parse_mode='HTML')



bot.polling()


