#!/usr/bin/python3
# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style


def unknown_input():
    unknowinput = 'Unknown input, fuck yourself ...'
    print(Style.BRIGHT + Fore.RED + unknowinput + Style.RESET_ALL)


def incorrect_input(userinput):
    incorrectinput = 'Could not understand '
    print(Style.BRIGHT + Fore.RED + incorrectinput + '\'' + userinput + '\'' + ' please try again.' + Style.RESET_ALL)


def ok():
    print(Style.DIM + Fore.GREEN + 'OK!' + Style.RESET_ALL)
