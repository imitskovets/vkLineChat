#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import echo_mess
import notification
from colorama import Fore, Back, Style


def dialog_chooser(max_dialog_number):
    chooser_input = input('Select number of dialog or \'-1\' to cancel: ')
    try:
        dialog_choose_answer = int(chooser_input)
    except ValueError:
        notification.incorrect_input(chooser_input)
        dialog_choose_answer = dialog_chooser(max_dialog_number)
        return dialog_choose_answer

    if -1 <= dialog_choose_answer <= max_dialog_number:
        return dialog_choose_answer
    else:
        notification.incorrect_input(str(dialog_choose_answer))
        return dialog_chooser(max_dialog_number)


def send_message(api, to_user_id, to_user_name):
    send_message_body = input('Message body(to \"' + to_user_name + '\"):\n\t')
    response = api.messages.send(user_id=to_user_id, message=send_message_body)
    return response


def show_dialog_with_user(dialog_need_to_show, api, user_name, my_name):
    history = api.messages.getHistory(rev=1, user_id=dialog_need_to_show['user_id'])
    '''start_message_id=start_id,'''
    for i in range(history['count']):
        echo_mess.one_mess_simple_view(history['items'][i], user_name, my_name)
    return 0


def show_unread_dialogs(api, my_name):
    dialogs = api.messages.getDialogs(unread=1)
    dialogs_count = dialogs['count']
    print('')
    print('You have ' + str(dialogs_count) + ' unread dialogs from')
    for i in range(dialogs_count):
        user_id = dialogs['items'][i]['message']['user_id']
        user = api.users.get(user_ids=user_id)[0]
        user_name = user['first_name'] + ' \t' + user['last_name']
        dialogs['items'][i]['message']['first_name'] = user['first_name']
        dialogs['items'][i]['message']['last_name'] = user['last_name']
        dialogs['items'][i]['message']['user_name'] = user_name
        print(str(i) + '. ' + str(dialogs['items'][i]['unread']) + '\t' + user_name + '\t\t\t' +
              time.strftime("%H:%M:%S %d.%m.%y", time.gmtime(dialogs['items'][i]['message']['date'])))
    answer = input('Do you want to see any of this dialogs? [y/n]: ')
    if answer == 'y' or answer == 'n':
        if answer == 'y':
            chosen_dialog = {'number': dialog_chooser(dialogs_count)}
            if chosen_dialog['number'] != -1:
                # print('you choose dialog number: ' + str(chosen_dialog['number']))
                chosen_dialog['user_id'] = dialogs['items'][chosen_dialog['number']]['message']['user_id']
                chosen_dialog['unread_count'] = dialogs['items'][chosen_dialog['number']]['unread']
                chosen_dialog['out_read_id'] = dialogs['items'][chosen_dialog['number']]['out_read']
                chosen_dialog['in_read_id'] = dialogs['items'][chosen_dialog['number']]['in_read']
                user = api.users.get(user_ids=str(chosen_dialog['user_id']))
                user_name = user[0]['first_name'] + ' \t' + user[0]['last_name']
                show_dialog_with_user(chosen_dialog, api, user_name, my_name)
                if 'y' == input('Do you want to answer?[y/n]'):
                    send_message(api, chosen_dialog['user_id'], "a nu i hui s nim")
                return chosen_dialog['user_id']
            else:
                return 0
        else:
            return 0
    else:
        notification.incorrect_input(answer)
        show_unread_dialogs(api, my_name)
    return 0
