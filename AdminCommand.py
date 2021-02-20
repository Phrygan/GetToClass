import util
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
    def run(cls):
        pass

class Show(AdminCommand):
    call = ['show']

    @classmethod
    def run(cls):
        pass

class ShowAmPm(AdminCommand):
    call = ['showampm']

    @classmethod
    def run(cls, *args):
        print("This week is: " + "AM" if util.am_pm_week == 0 else "PM")

class Stop(AdminCommand):
    call = ['stop']

    @classmethod
    def run(cls, bot_thread):
        exit()

class Reboot(AdminCommand):
    call = ['reboot']

    @classmethod
    def run(cls):
        pass

AdminCommand.admin_commands = AdminCommand.__subclasses__()