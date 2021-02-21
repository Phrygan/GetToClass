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

class Show(AdminCommand):
    call = ['show']

    @classmethod
    def run(cls, *args):
        pass
        # if args[0] == None:
        #     print_log(ADMIN_COMMAND_LOG_TYPE, ADMIN_SUPPORTED_VARIABLES)
        #     print_log(ADMIN_COMMAND_LOG_TYPE, 'Usage:\nshow [-a] [--all] [<variable_name>]')
        # elif args[0] in ['-a', '--all']:
        #     print_log(ADMIN_COMMAND_LOG_TYPE, ADMIN_SUPPORTED_VARIABLES)
        # elif args[0] in ADMIN_SUPPORTED_VARIABLES.keys():
        #     print_log(ADMIN_COMMAND_LOG_TYPE, 
        #               f'{args[0]}: {ADMIN_SUPPORTED_VARIABLES[args[0]]}')
        # else:
        #     print_log(ADMIN_COMMAND_LOG_TYPE, f'show does not support {args[0]}')

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
        pass

AdminCommand.admin_commands = AdminCommand.__subclasses__()