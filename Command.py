import asyncio
import util

class Command():
    commands = []

class Create_Profile(Command):
    call = [">createprofile", ">cp"]

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
    call = [">setlink", ">sl", "addlink"]

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
    call = [">deleteprofile", ">deletelink", ">delete", "del"]

    @staticmethod
    @util.update_link_data
    async def run(message, *args):
        command_args = message.content.split(' ')
        if(command_args[1]):
            util.link_data[str(message.author.id)][int(command_args[1])-1] = ''
            await message.reply("Link for period " + command_args[1] + " has been deleted")
            util.print_log("link_data/edit", f"{message.author.id} has deleted class period {command_args[1]}")
            return
        del util.link_data[str(message.author.id)]
        await message.reply(str(message.author.id) + "'s profile has been deleted.")
        util.print_log("link_data/edit", f"{message.author.id} has deleted their profile")

class Change_Am_Pm_week(Command):
    call = [">changeampmweek", ">capw"]

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
    call = [">viewprofile", ">vp"]

    @staticmethod
    async def run(message, *args):
        print(message.author.id)

        try:
            msg='\n'.join([f"{period + 1}: {util.link_data[str(message.author.id)][period]}" for period in range(8)])
            await message.reply("Here is a list of all of your class zoom links:\n\n" + msg)
        except:
            await message.reply("User not found in GET TO CLASS Database! Do >createprofile first and add links!")

Command.commands = Command.__subclasses__()

    
