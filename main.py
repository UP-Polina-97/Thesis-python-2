### basic code from the assignment
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Vk_information import GetInfoFromVk, GetPhotosVkData

#token = ''
token = input('Token for group: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

user_id_fromWR = []

def BotWriteMsg(user_id, message):
    """THis is a bot that can help you to find love"""
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                BotWriteMsg(event.user_id,
                          f"Привет я бот для try try me. Я могу помочь вам найти пару :D")
                user_id_fromWR.append(event.user_id)
                print(GetInfoFromVk(user_id_fromWR))
                print(GetPhotosVkData(user_id_fromWR))
            elif request == "пока":
                BotWriteMsg(event.user_id, "Пока((")
            else:
                BotWriteMsg(event.user_id, "Не поняла вашего ответа...")


