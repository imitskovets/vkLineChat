#!/usr/bin/python3
# -*- coding: utf-8 -*-

import getpass

from colorama import Fore
from colorama import Style

import notification
import vk_auth

# our application identification
appid = '5589908'


def vk_token():
    userlogin = input('Enter your e-mail or phone number: ')
    userpassword = getpass.getpass(prompt="...and password:")
    # TODO  add exception
    # permissions for our app
    auth_content = vk_auth.auth(userlogin, userpassword, appid, "offline,messages")
    notification.ok()
    return auth_content


def new_session():
    auth_content = vk_token()
    output_auth_file = open('auth_content', 'w')
    output_auth_file.write(auth_content[0] + ' ' + auth_content[1])
    output_auth_file.close()
    return auth_content


def old_session():
    try:
        input_auth_file = open("auth_content")
        auth_content = input_auth_file.readline().split(" ")
        input_auth_file.close()
        if len(auth_content[0]) < 85:
            print(Style.DIM + Fore.RED + 'File is empty! Starts new session ...' + Style.RESET_ALL)
            auth_content = new_session()
    except IOError:
        print(Style.DIM + Fore.RED + "No session found! Starts new session ..." + Style.RESET_ALL)
        auth_content = new_session()
    return auth_content


def new_old_session_menu():
    answer = input('Try to continue old session? [y/n] : ')
    auth_content = []
    if answer == 'y' or answer == 'n' or answer == 'н' or answer == 'т':
        if answer == 'y' or answer == 'н':
            auth_content = old_session()
        if answer == 'n' or answer == 'т':
            auth_content = new_session()
    else:
        notification.unknown_input()
        exit(1)
    return auth_content
