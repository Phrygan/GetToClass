import asyncio
import util

class Command():
    commands = []

class Create_Profile(Command):
    call = [">createprofile"]

    @classmethod
    async def run(cls, message, *args):
        util.link_data[str(message.author.id)] = ["" for i in range(8)]
        util.edit_link_data(util.link_data)
        await message.reply("Created your profile!")

class Set_Link(Command):
    call = [">setlink"]

    @classmethod
    async def run(cls, message, *args):
        args = message.content.split(' ')
        try:
            util.link_data[str(message.author.id)][int(args[2])-1] = args[1]
            util.edit_link_data(util.link_data)
        except:
            if (not args[2]):
                await message.reply("Please provide a link and its corresponding period number!")
                return 
            await message.reply("Do >create_profile first!")

        print("All Link Information >> ", util.link_data)

        await message.reply("Added link for " + str(message.author))

class Delete_Profile(Command):
    call = [">deleteprofile"]

    @classmethod
    async def run(cls, message, *args):
        del util.link_data[str(message.author.id)]
        util.edit_link_data(util.link_data)
        await message.reply(str(message.author.id) + "'s profile has been deleted.")

class Change_Am_Pm_week(Command):
    call = [">changeampmweek"]

    @classmethod
    async def run(cls, message, *args):
        command_args = message.content.split(' ')
        if(await util.check_for_role(args[0], util.ROLE_VOLUNTEER, message.author.id)):
            if(command_args[1] == 'am'):
                am_pm_week = 0
            elif(command_args[1] == 'pm'):
                am_pm_week = 1
            print("\nam_pm_week is now set to >> " + str(am_pm_week))

Command.commands = Command.__subclasses__()

    
