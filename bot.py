import os
import discord
import time
import datetime
import asyncio
from threading import Thread

import util
from Command import Command
from AdminCommand import AdminCommand

client = discord.Client()

async def send_interval_message():
    await client.wait_until_ready()
    interval = 60
    while not client.is_closed():
        if(util.is_enabled):
            timeFormatted = datetime.datetime.now().strftime("%H:%M")
            currentBlock = None
            for y in range(len(util.BLOCK_TIMES)):
                if util.BLOCK_TIMES[y] == timeFormatted:
                    currentBlock = y + 1
                    break
            if currentBlock:
                currentPeriod = util.block_to_period(currentBlock)
                if currentPeriod:
                    util.print_log("currentPeriod/change", f"Current Period is now {currentPeriod}")
                    for userid in util.link_data.keys():
                        if(not util.user_settings[userid] or (util.user_settings[userid] and currentBlock > 4)):
                            util.print_log("message", f"messaging {userid} their class link")
                            classLink = util.link_data[userid][currentPeriod-1]
                            userprofile = await client.fetch_user(userid)
                            dm_embed = discord.Embed(
                                title = 'JOIN YOUR CLASS HERE!',
                                colour = util.get_color(userid)
                            )
                            if(len(classLink.content.split(' ')) > 1):
                                class_link_list = classLink.content.split(' ')
                                dm_embed.add_field(name=f'Period {currentPeriod}', value=f'Link: {class_link_list[0]}', inline=True)
                                for class_link_input_embed in class_link_list:
                                    if(class_link_input_embed != class_link_list[0]):
                                        dm_embed.add_field(name=f'Alternate Link[s]', value=f'Link: {class_link_list[0]}', inline=True)
                            else:
                                dm_embed.add_field(name=f'Period {currentPeriod}', value=f'Link: {classLink}', inline=True)
                            try:
                                await userprofile.send(embed=dm_embed)
                            except:
                                util.print_log("error/blocked", f"Person causing problem is {userid}")
        await asyncio.sleep(interval)
                
def admin_terminal():
    while not client.is_closed():
        admin_in = input()
        if ' ' in admin_in:
            admin_in.split(' ')
            admin_command_call = admin_in[0]
            admin_command_args = admin_in[1:]
        else:
            admin_command_call = admin_in
            admin_command_args = None
        for admin_command in AdminCommand.admin_commands:
            if admin_command_call in admin_command.call:
                admin_command.run(admin_command_args)

@client.event
async def on_ready():
    print("Discord bot is ONLINE")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("ver 1.0"))
    client.loop.create_task(send_interval_message())

@client.event
async def on_message(message):
    args = message.content.split(' ')
    for command in Command.commands:
        if args[0] in command.call:
            await command.run(message, client)

def main():

    loop = asyncio.get_event_loop()
    loop.create_task(client.start(util.get_discord_key()))
    Thread(target=loop.run_forever())

    # print("Discord bot booting (this may take a few seconds)...")
    # discord_bot_thread = Thread(
    #     target=client.run, 
    #     args=(util.get_discord_key(), ),
    #     daemon=True)
    # discord_bot_thread.start()
    # admin_terminal()
    
# if __name__ == '__main__':
#     main()

main()
