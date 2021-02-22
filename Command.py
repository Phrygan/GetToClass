import asyncio
import util

class Command():
    commands = []

class Create_Profile(Command):
    call = [">createprofile"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        util.link_data[str(message.author.id)] = ["" for i in range(8)]
        await message.reply("Created your profile!")
        util.print_log("link_data/edit", f"{message.author.id} has initialized their profile")

class Set_Link(Command):
    call = [">setlink"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        args = message.content.split(' ')
        try:
            util.link_data[str(message.author.id)][int(args[2])-1] = args[1]
        except:
            if (not args[2]):
                await message.reply("Please provide a link and its corresponding period number!")
                return 
            await message.reply("Do >createprofile first!")

        util.print_log("link_data/edit", f"{message.author.id} has added a link")

        await message.reply("Added link for " + str(message.author))

class Delete_Profile(Command):
    call = [">deleteprofile"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        del util.link_data[str(message.author.id)]
        await message.reply(str(message.author.id) + "'s profile has been deleted.")
        util.print_log("link_data/edit", f"{message.author.id} has deleted their profile")

class Change_Am_Pm_week(Command):
    call = [">changeampmweek"]

    @staticmethod
    async def run(message, *args):
        command_args = message.content.split(' ')
        if(await util.check_for_role(args[0], util.ROLE_VOLUNTEER, message.author.id)):
            if(command_args[1] == 'am'):
                am_pm_week = 0
            elif(command_args[1] == 'pm'):
                am_pm_week = 1
            util.print_log("am_pm_week/edit", f"{message.author.id} has adjusted am_pm_week to {am_pm_week}")

Command.commands = Command.__subclasses__()

    
