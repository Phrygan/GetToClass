import os
import sys

from util import *

"""
commands to add:
    stop
    clearlog
    show variable_name
    reboot
"""

class AdminCommand():
    admin_commands = []

class ClearLog(AdminCommand):
    call = ['clearlog']

    @classmethod
    def run(cls, *args):
        with open('log.txt', 'w+') as log_file:
            log_file.write(str())
        print_log(ADMIN_COMMAND_LOG_TYPE, "Log cleared")

class ShowAmPm(AdminCommand):
    call = ['showampm']

    @classmethod
    def run(cls, *args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "This week is " + "AM" if am_pm_week == 0 else "PM")

class Stop(AdminCommand):
    call = ['stop']

    @classmethod
    def run(cls, bot_thread, *args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "Stopping discord bot")
        exit()

class Reboot(AdminCommand):
    call = ['reboot']

    @classmethod
    def run(cls, *args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "Discord bot rebooting (this may take a few seconds)...\n")
        os.system('python bot.py')
        exit()

AdminCommand.admin_commands = AdminCommand.__subclasses__()