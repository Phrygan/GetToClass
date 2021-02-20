import os
import discord
import time
import datetime
import asyncio

import util
import Command

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

client.run("Nzk5NzYyMzUzMjU1NDgxMzg0.YAISuw.SXOXjdmOd5qyzVUVWeA1c6Z4En4")


