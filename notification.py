#!/usr/bin/python3
# -*- coding: utf-8 -*-
from colorama import Fore, Style


def unknown_input():
    unknowinput = 'Unknown input, fuck yourself ...'
    print(Style.BRIGHT + Fore.RED + unknowinput + Style.RESET_ALL)
    return 0


def incorrect_input(userinput):
    incorrectinput = 'Could not understand '
    print(Style.BRIGHT + Fore.RED + incorrectinput + '\'' + userinput + '\'' + ' please try again.' + Style.RESET_ALL)
    return 0


def ok():
    print(Style.DIM + Fore.GREEN + 'OK!' + Style.RESET_ALL)
    return 0


def color_tests():
    print(Fore.GREEN + 'green')
    print(Fore.LIGHTGREEN_EX + 'lig_green')
    print(Fore.RED + 'red')
    print(Fore.LIGHTRED_EX + 'li_red')
    print(Fore.BLACK + 'black')
    print(Fore.LIGHTBLACK_EX + 'li_black')
    print(Fore.BLUE + 'blue')
    print(Fore.LIGHTBLUE_EX + 'li_blue')
    print(Fore.YELLOW + 'yellow')
    print(Fore.LIGHTYELLOW_EX + 'li_yellow')
    print(Fore.MAGENTA + 'magenta')
    print(Fore.LIGHTMAGENTA_EX + 'li_magenta')
    print(Fore.CYAN + 'cyan')
    print(Fore.LIGHTCYAN_EX + 'li_cyan')
    print(Fore.WHITE + 'white')
    print(Fore.LIGHTWHITE_EX + 'li_white')
    print(Style.DIM)
    print(Fore.GREEN + 'green')
    print(Fore.LIGHTGREEN_EX + 'lig_green')
    print(Fore.RED + 'red')
    print(Fore.LIGHTRED_EX + 'li_red')
    print(Fore.BLACK + 'black')
    print(Fore.LIGHTBLACK_EX + 'li_black')
    print(Fore.BLUE + 'blue')
    print(Fore.LIGHTBLUE_EX + 'li_blue')
    print(Fore.YELLOW + 'yellow')
    print(Fore.LIGHTYELLOW_EX + 'li_yellow')
    print(Fore.MAGENTA + 'magenta')
    print(Fore.LIGHTMAGENTA_EX + 'li_magenta')
    print(Fore.CYAN + 'cyan')
    print(Fore.LIGHTCYAN_EX + 'li_cyan')
    print(Fore.WHITE + 'white')
    print(Fore.LIGHTWHITE_EX + 'li_white')
    print(Style.RESET_ALL)
    print(Style.BRIGHT)
    print(Fore.GREEN + 'green')
    print(Fore.LIGHTGREEN_EX + 'lig_green')
    print(Fore.RED + 'red')
    print(Fore.LIGHTRED_EX + 'li_red')
    print(Fore.BLACK + 'black')
    print(Fore.LIGHTBLACK_EX + 'li_black')
    print(Fore.BLUE + 'blue')
    print(Fore.LIGHTBLUE_EX + 'li_blue')
    print(Fore.YELLOW + 'yellow')
    print(Fore.LIGHTYELLOW_EX + 'li_yellow')
    print(Fore.MAGENTA + 'magenta')
    print(Fore.LIGHTMAGENTA_EX + 'li_magenta')
    print(Fore.CYAN + 'cyan')
    print(Fore.LIGHTCYAN_EX + 'li_cyan')
    print(Fore.WHITE + 'white')
    print(Fore.LIGHTWHITE_EX + 'li_white')
    print(Style.RESET_ALL)
    return 0
