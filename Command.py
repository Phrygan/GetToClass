import asyncio
import util

class Command():
    commands = []

class Create_Profile(Command):
    call = [">createprofile"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        if str(message.author.id) not in util.link_data:
            util.link_data[str(message.author.id)] = ["" for i in range(8)]
            await message.reply("Created your profile!")
            util.print_log("link_data/edit", f"{message.author.id} has initialized their profile")
        else:
            await message.reply("You already have a profile silly!")

class Set_Link(Command):
    call = [">setlink"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        command_args = message.content.split(' ')
        try:
            util.link_data[str(message.author.id)][int(command_args[2])-1] = command_args[1]
        except:
            if len(command_args) != 3:
                await message.reply("Please provide a link and its corresponding period number! Check how #how-to-use for details")
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

class View_Links(Command):
    call = [">viewprofile"]

    @staticmethod
    async def run(message, *args):
        authorid = str(message.author.id)
        await message.reply(f'''The links for your classes are:
        1: {util.link_data[authorid][0]}
        2: {util.link_data[authorid][1]}
        3: {util.link_data[authorid][2]}
        4: {util.link_data[authorid][3]}
        5: {util.link_data[authorid][4]}
        6: {util.link_data[authorid][5]}
        7: {util.link_data[authorid][6]}
        8: {util.link_data[authorid][7]}''')

Command.commands = Command.__subclasses__()

    
