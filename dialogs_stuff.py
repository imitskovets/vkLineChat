#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import echo_mess
import notification


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


def mark_message_as_read_verb(api, last_id, user_id):
    leave_mess = input('How many messages do want to leave unread? : ')
    target_read_mes_id = \
        api.messages.getHistory(count=1, user_id=user_id, offset=leave_mess, start_message_id=last_id)['items'][0]['id']
    api.messages.markAsRead(message_ids=target_read_mes_id)


def send_message(api, to_user_id, to_user_name, my_name):
    send_message_body = input('Message body(to \"' + to_user_name + '\"):\n')
    response = api.messages.send(user_id=to_user_id, message=send_message_body)
    message = dict(out=1, body=send_message_body, read_state=0, date=int(api.utils.getServerTime()))
    echo_mess.one_mess_simple_view(message, to_user_name, my_name)

    return response


def show_dialog_with_user(dialog_need_to_show, api, my_name):
    # the count of messages shown above the read one
    # TODO move add_mess in config
    add_mes = 5
    count = dialog_need_to_show['last_id'] - dialog_need_to_show['in_read'] + add_mes
    history = api.messages.getHistory(count=count, user_id=dialog_need_to_show['user_id'])
    for i in range(count - 1, -1, -1):
        echo_mess.one_mess_simple_view(history['items'][i], dialog_need_to_show['user_name'], my_name)
    return 0


def show_unread_dialogs(api, my_name):
    dialogs = api.messages.getDialogs(unread=1)
    print('')
    if dialogs['count'] == 0:
        print('You have no new messages :( .')
        print('You have no friends, you useless.. Try to kill youself, maybe it will make the world better')
        return 0
    print('You have ' + str(dialogs['count']) + ' unread dialogs from')
    for i in range(dialogs['count']):
        user = api.users.get(user_ids=dialogs['items'][i]['message']['user_id'])[0]
        dialogs['items'][i]['message']['first_name'] = user['first_name']
        dialogs['items'][i]['message']['last_name'] = user['last_name']
        dialogs['items'][i]['message']['user_name'] = user['first_name'] + ' \t' + user['last_name']
        print(str(i) + '. ' + str(dialogs['items'][i]['unread']) + '\t' + user['first_name'] + ' \t' +
              user['last_name'] + '\t\t\t' +
              time.strftime("%H:%M:%S %d.%m.%y", time.gmtime(dialogs['items'][i]['message']['date'])))
    answer = input('Do you want to see any of this dialogs? [y/n]: ')
    if answer == 'y' or answer == 'n' or answer == 'т' or answer == 'н':
        if answer == 'y' or answer == 'н':
            chosen_dialog = {'number': dialog_chooser(dialogs['count'])}
            if chosen_dialog['number'] != -1:
                chosen_dialog['user_id'] = dialogs['items'][chosen_dialog['number']]['message']['user_id']
                chosen_dialog['unread_count'] = dialogs['items'][chosen_dialog['number']]['unread']
                chosen_dialog['out_read_id'] = dialogs['items'][chosen_dialog['number']]['out_read']
                chosen_dialog['in_read'] = dialogs['items'][chosen_dialog['number']]['in_read']
                user = api.users.get(user_ids=str(chosen_dialog['user_id']))
                chosen_dialog['user_name'] = user[0]['first_name'] + ' \t' + user[0]['last_name']
                chosen_dialog['user_last_name'] = user[0]['last_name']
                chosen_dialog['user_first_name'] = user[0]['first_name']
                chosen_dialog['last_id'] = dialogs['items'][chosen_dialog['number']]['message']['id']
                show_dialog_with_user(chosen_dialog, api, my_name)
                answer = input('Do you want to answer?[y/n] ')
                if answer == 'y' or answer == 'n' or answer == 'т' or answer == 'н':
                    if answer == 'y' or answer == 'н':
                        send_message(api, chosen_dialog['user_id'], chosen_dialog['user_name'], my_name)
                    if answer == 'n' or answer == 'т':
                        answer = input('Do you want to mark messages as read?[y/n] ')
                        if answer == 'y' or answer == 'n' or answer == 'т' or answer == 'н':
                            if answer == 'y' or answer == 'н':
                                mark_message_as_read_verb(api, chosen_dialog['last_id'], chosen_dialog['user_id'])
                            else:
                                notification.unknown_input()
                else:
                    notification.unknown_input()

                return chosen_dialog['user_id']
            else:
                return 0
        else:
            return 0
    else:
        notification.incorrect_input(answer)
        show_unread_dialogs(api, my_name)
    return 0
