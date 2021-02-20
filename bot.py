import os
import discord
import time
import datetime
import asyncio
from threading import Thread

import util
import Command
import AdminCommand

client = discord.Client()

async def send_interval_message():
    await client.wait_until_ready()
    interval = 60
    while not client.is_closed():
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
                    util.print_log("message", f"messaging {userid} their class link")
                    classLink = util.link_data[userid][currentPeriod-1]
                    userprofile = await client.fetch_user(userid)
                    await userprofile.send("Join Your Class Here: " + classLink)
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
        print(f'actual: {util.am_pm_week}')
        for admin_command in AdminCommand.AdminCommand.admin_commands:
            if admin_command_call in admin_command.call:
                admin_command.run(admin_command_args)

@client.event
async def on_ready():
    print("Bot is ONLINE\n")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("ver 0.0"))
    client.loop.create_task(send_interval_message())

@client.event
async def on_message(message):
    args = message.content.split(' ')
    for command in Command.Command.commands:
        if args[0] in command.call:
            await command.run(message, client)

def main():
    discord_bot_thread = Thread(
        target=client.run, 
        args=("Nzk5NzYyMzUzMjU1NDgxMzg0.YAISuw.SXOXjdmOd5qyzVUVWeA1c6Z4En4", ),
        daemon=True)
    discord_bot_thread.start()
    admin_terminal()
    

if __name__ == '__main__':
    main()

