import util

class AdminCommand():
    admin_commands = []

class ShowAmPm(AdminCommand):
    call = ["showampm"]

    @classmethod
    def run(cls, *args):
        print("This week is: " + "AM" if util.am_pm_week == 0 else "PM")



AdminCommand.admin_commands = AdminCommand.__subclasses__()