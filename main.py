### basic code from the assignment
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Vk_information import get_users_for_date

token = input('Token for groupchat in vk: ')


vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

user_id_fromWR = []

def BotWriteMsg(user_id, message):
    """THis is a bot that can help you to find love give messages"""
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(10 ** 7),})

def BotSendPhoto(user_id, message, url):
    """THis is a bot that can help you to find love give photos"""
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'attachment': url,
        'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                BotWriteMsg(event.user_id,
                          f"Привет я бот для try try me. Я могу помочь вам найти пару. Вам помочь? :D")
                user_id_fromWR.append(event.text)
            elif request == "да":
                BotWriteMsg(event.user_id, "Какой вай возвратной диапазон? \n 1. 18-24 лет"
                                           "\n2. 25-34 лет"
                                           "\n3. 35-44 лет"
                                           "\n4. 45-54 лет"
                                           "\n5. 55-64 лет"
                                           "\n6. 65-74 лет "
                                           "\n7. 75 лет и старше "
                                           "\nПожалуйста выберите любой из этих категорий и напишите номер в чат. :-)")
            elif request == '1':
                photo, name, id_of_person = get_users_for_date(event.user_id, 1)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '2':
                photo, name, id_of_person = get_users_for_date(event.user_id, 2)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '3':
                photo, name, id_of_person = get_users_for_date(event.user_id, 3)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '4':
                photo, name, id_of_person = get_users_for_date(event.user_id, 4)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '5':
                photo, name, id_of_person = get_users_for_date(event.user_id, 5)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '6':
                photo, name, id_of_person = get_users_for_date(event.user_id, 6)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == '7':
                photo, name, id_of_person = get_users_for_date(event.user_id, 7)
                for n, i, p in zip(name, id_of_person, photo):
                    BotSendPhoto(event.user_id, f"{n} https://vk.com/id{i} \n", p)
            elif request == "пока":
                BotWriteMsg(event.user_id, "Пока((")
            else:
                BotWriteMsg(event.user_id, "Не поняла вашего ответа...")


