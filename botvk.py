from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
token ="5c35c0a80ecfc06191d414a3201c8361ab74edf062a0e2b6e04a728173f0d0ac6d890d9b34d3e04bcd7ba"
vk_session = vk_api.VkApi(token=token)
session_api=vk_session.get_api()
longpoll=VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения : " +str(event.text))
