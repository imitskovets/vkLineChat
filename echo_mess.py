#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

from colorama import Fore, Style


def one_mess_simple_view(message, user_name, my_name):
    '''
    user_name = api.users.get(user_ids=message['user_id'])[0]['first_name'] + \
                api.users.get(user_ids=message['user_id'])[0]['last_name']
    '''
    out_pre = '\t'
    if message['out'] == 1:
        out_pre += '\t'
        name = my_name
    else:
        name = user_name
    if message['read_state'] == 0:
        print(out_pre + name)
        print(out_pre + time.strftime("%d.%m\t%H:%M:%S", time.gmtime(message['date'])), end='')
        print(Style.DIM + Fore.LIGHTBLUE_EX + ' ⏺' + Style.RESET_ALL)
    else:
        print(out_pre + name)
        print(out_pre + time.strftime("%d.%m\t%H:%M:%S", time.gmtime(message['date'])))
    # if message['title'] != ' ... ':
    #   print('\t' + 'Title : ' + message['title'])
    print(out_pre + '\t' + message['body'])
    print('')
    return 0
