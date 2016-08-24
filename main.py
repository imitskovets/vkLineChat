#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk
import dialogs_stuff
import notification
import token_stuff
from colorama import init
from colorama import Fore, Back, Style

init()
appid = '5589908'
auth_content = token_stuff.new_old_session_menu()
accesstoken = auth_content[0]
myid = auth_content[1]
session = vk.Session()
api = vk.API(session, v='5.53', lang='ru', access_token=accesstoken)
me = api.users.get(user_ids=str(myid))
my_name = me[0]['first_name'] + ' \t' + me[0]['last_name']
print(Style.DIM + Fore.LIGHTGREEN_EX + 'So, now we are ready to chat!' + Style.RESET_ALL)
chosen_user_id = dialogs_stuff.show_unread_dialogs(api, my_name)




'''
received_mess = api.messages.get(count=recMesCount, out=0, time_offset=0)
print(api.messages.markAsRead(message_ids=(received_mess['items'][0]['id'])))
'''
print('Bye... Bye...')
