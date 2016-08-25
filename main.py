#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk
from colorama import Fore, Style
from colorama import init

import dialogs_stuff
import token_stuff

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


#notification.color_tests()

print('Bye... Bye...')
