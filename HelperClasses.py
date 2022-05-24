from telebot.apihelper import ApiTelegramException
class Verifier:

    def __init__(self,bot):
        self.bot = bot


    def set_chat_id_dic(self,chat_id_dic):
        self.chat_id_dic = chat_id_dic


    def is_subscribed(self, chat_id, user_id):
        try:
            member = self.bot.get_chat_member(chat_id, user_id)
        except ApiTelegramException as e:
            if e.result_json['description'] == 'Bad Request: user not found':
                return False
        if member.status == "left":
            return False
        return True


    def result(self,user_id):
        if not self.is_subscribed(self.chat_id_dic["Group"],user_id):
            # print(self.chat_id_dic["Group"])
            return False
        if not self.is_subscribed(self.chat_id_dic["Channel"],user_id):
            print(self.chat_id_dic["Channel"])
            return False
        return True
