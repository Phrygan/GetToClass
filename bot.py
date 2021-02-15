import os
import discord
import datetime
import time
import asyncio
import json

'''
import json


def write_to_json_file(data={}):
    with open('linkdata.json') as json_file:
        json_data = json_file.read()
        json_data_formatted = json.loads(json_data)

    with open('linkdata.json', 'w+') as json_file:
        json_data_formatted.update(data)
        json.dump(json_data_formatted, json_file)
'''

client = discord.Client()
timeNow = datetime

Linkdata = {
    "exampleid": ["example.com"]
}
Classtime = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

block_times = ["7:57", "8:57", "9:57", "10:57", "13:07", "13:57"]
block_period_data = [ 
    [
        [1,2,3,4,5,6],
        [1,2,3,4,7,8],
        [1,2,3,4], 
        [5,6,7,8,1,2], 
        [5,6,7,8,3,4]
    ],
    [
        [1,2,3,4,5,6],
        [1,2,3,4,7,8],
        [5,6,7,8], 
        [5,6,7,8,1,2], 
        [5,6,7,8,3,4]
    ]
]

am_pm_week = 0

def block_to_period(block):
    time_week_day = timeNow.datetime.now().strftime("%w")

    if(time_week_day == 5 or time_week_day == 6):
        print("It's a weekend! F*** off!")
        return 

    try:
        return block_period_data[am_pm_week][int(time_week_day)][block-1]
    except:
        print("\nThe day number is >>" + str(int(time_week_day)-1))
        return

async def send_interval_message():
    await client.wait_until_ready()
    interval = 60
    while not client.is_closed():

        timeFormatted = timeNow.datetime.now().strftime("%H:%M")
        currentBlock = None

        for y in range(len(block_times)):
            if block_times[y] == timeFormatted:
                currentBlock = y + 1
                print("The block has changed !!! >> " + str(currentBlock))
                break

        if currentBlock:

            currentPeriod = block_to_period(currentBlock)

            if currentPeriod:
                print("\nThe period has changed !!! >> " + str(currentPeriod) + "\n")
                
                for x in range(len(Classtime[currentPeriod-1])):

                    userid = Classtime[currentPeriod-1][x]
                    print("messaging this user >> " + str(userid))

                    idperiod = userid.split("|")

                    classLink = Linkdata[int(idperiod[0])][int(idperiod[1])-1]
                    userprofile = await client.fetch_user(int(idperiod[0]))
                    await userprofile.send("Join Your Class Here: " + classLink)
                
                print("\n")

        await asyncio.sleep(interval)

@client.event
async def on_ready():
    print("Bot is ONLINE\n")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("ver 0.0.1"))
    client.loop.create_task(send_interval_message())

@client.event
async def on_message(message):
    args = message.content.split(' ')

    if (args[0] == ">createprofile"):
        Linkdata[message.author.id] = []
        await message.reply("Created your profile!")

    if(args[0] == '>setlink'):

        try:
            Linkdata[message.author.id].append(args[1])

        except:
            await message.reply("Do >createprofile first! :)")
            return

        try:
            Classtime[int(args[2])-1].append(str(message.author.id) + " | " + args[2])

        except:
            print("an error has happened")

        print("All Link Information >> ", Linkdata)
        print("All Classtime Infromation >> ", Classtime, "\n")

        await message.reply("Added link for " + str(message.author))

    if (message.content.startswith('>deleteprofile')):

        del Linkdata[message.author.id]
        await message.reply(str(message.author.id) + "'s profile has been deleted")

        for y in range(len(Classtime)):
            try:
                Classtime[y].remove(str(message.author.id) + "|" + str(y+1))
            except:
                pass

client.run("Nzk5NzYyMzUzMjU1NDgxMzg0.YAISuw.SXOXjdmOd5qyzVUVWeA1c6Z4En4")


