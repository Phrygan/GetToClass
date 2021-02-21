import os
import sys

from util import *

class AdminCommand():
    admin_commands = []

class ClearLog(AdminCommand):
    call = ['clearlog']
    @staticmethod
    def run(*args):
        with open('log.txt', 'w+') as log_file:
            log_file.write(str())
        print_log(ADMIN_COMMAND_LOG_TYPE, "Log cleared")

class ShowAmPm(AdminCommand):
    call = ['showampm']
    @staticmethod
    def run(*args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "This week is " + "AM" if am_pm_week == 0 else "PM")

class Stop(AdminCommand):
    call = ['stop']
    @staticmethod
    def run(bot_thread, *args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "Discord bot stopping")
        exit()

class Reboot(AdminCommand):
    call = ['reboot']
    @staticmethod
    def run(*args):
        print_log(ADMIN_COMMAND_LOG_TYPE, "Discord bot rebooting...\n")
        os.system('python -m bot')
        exit()

AdminCommand.admin_commands = AdminCommand.__subclasses__()