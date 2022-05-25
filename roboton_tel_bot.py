from constants import API_KEY
from constants import defaults_messages
from constants import chat_id_dic
from HelperClasses import Verifier
from json_handler import JsonDataBase
import telebot
import random


bot = telebot.TeleBot(API_KEY)
verifier = Verifier(bot)
json_db = JsonDataBase()

verifier.set_chat_id_dic(chat_id_dic)


def get_user_data(uid, wallet_addr):
    user_id = uid
    wallet_address = wallet_addr
    status = "verified"
    chance = 1
    code = get_refcode()
    udata = {
        "uid": user_id,
        "wallet_addr": wallet_address,
        "status": status,
        "ref_code": code,
        "chance": chance,
    }
    return udata


def get_refcode():
    chars = "6NxCKsuzFnGWJZToa9qbEyX23ALSHjRim4vfhIOB8ldcVwU5pg7Yr01ekPDQtM"
    code = ""
    while len(code) != 12:
        letter = random.choice(list(chars))
        if letter not in code:
            code += letter
    return code


@bot.message_handler(commands=["start"])
def send_start_msg(message):
    bot.send_message(message.chat.id, defaults_messages["start"], parse_mode="HTML")


@bot.message_handler(commands=["verify"])
def send_verification_result(message):
    if verifier.result(message.from_user.id) is True:
        bot.send_message(
            message.chat.id, defaults_messages["verified_msg"], parse_mode="HTML"
        )
    else:
        bot.send_message(
            message.chat.id, defaults_messages["verify_error"], parse_mode="HTML"
        )


def is_valid(wallet_addr):
    if len(wallet_addr) != 48:
        return False
    if wallet_addr[0:2] != "EQ":
        return False
    return True


@bot.message_handler(func=lambda msg: msg.content_type == "text")
def get_wallet_addr(msg):
    wallet_address = msg.text
    if verifier.result(msg.from_user.id) is False:
        bot.send_message(
            msg.chat.id, defaults_messages["verify_error"], parse_mode="HTML"
        )
        return 0
    if is_valid(wallet_address):
        # save wallet then
        user_data = get_user_data(msg.from_user.id, wallet_address)
        result = json_db.store_user_data(user_data)
        if result == 0:
            bot.send_message(msg.chat.id, defaults_messages["wallet_exist"])
        if result == 1:
            bot.send_message(msg.chat.id, defaults_messages["wallet_added"])


bot.polling()
