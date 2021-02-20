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
BLOCK_TIMES = ["7:57", "8:57", "9:57", "10:57", "13:07", "13:52"]
BLOCK_PERIOD_DATA = [ 
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
ROLE_VOLUNTEER = 811698025600122942
GUILD_ID = 799773078557163541
LINKDATA_FILE = 'linkdata.json'

def read_link_data():
    with open(LINKDATA_FILE) as json_file:
        link_data_json = json_file.read()
        link_data = json.loads(link_data_json)
        print(link_data)
        return link_data
Linkdata = read_link_data()

def edit_link_data(Linkdata):
    with open(LINKDATA_FILE, 'w+') as json_file:
        json.dump(Linkdata, json_file)

def block_to_period(block):
    time_week_day = datetime.datetime.now().strftime("%w")
    if(time_week_day == 5 or time_week_day == 6):
        print("It's a weekend! F*** off!")
        return 
    try:
        return BLOCK_PERIOD_DATA[am_pm_week][int(time_week_day)-1][block-1]
    except:
        print("\nThe day number is >>" + str(int(time_week_day)-1))

async def check_for_role(role, userid):
    server = client.get_guild(GUILD_ID)
    user_member = await server.fetch_member(userid)
    for user_role in user_member.roles:
        if(user_role.id == role):
            return True
    return False

async def create_profile(message):
    Linkdata[str(message.author.id)] = ["" for i in range(8)]
    edit_link_data(Linkdata)
    await message.reply("Created your profile!")

async def set_link(message):
    args = message.content.split(' ')
    try:
        Linkdata[str(message.author.id)][int(args[2])-1] = args[1]
        edit_link_data(Linkdata)
    except:
        if (not args[2]):
            await message.reply("Please provide a link and its corresponding period number!")
            return 
        await message.reply("Do >create_profile first!")

    print("All Link Information >> ", Linkdata)

    await message.reply("Added link for " + str(message.author))

async def delete_profile(message):
    del Linkdata[str(message.author.id)]
    edit_link_data(Linkdata)
    await message.reply(str(message.author.id) + "'s profile has been deleted.")

async def am_pm_week(message):

    args = message.content.split(' ')

    if(await check_for_role(ROLE_VOLUNTEER, message.author.id)):
        if(args[1] == 'am'):
            am_pm_week = 0
        elif(args[1] == 'pm'):
            am_pm_week = 1
        print("\nam_pm_week is now set to >> " + str(am_pm_week))

async def send_interval_message():
    await client.wait_until_ready()
    interval = 60
    while not client.is_closed():
        timeFormatted = datetime.datetime.now().strftime("%H:%M")
        currentBlock = None
        for y in range(len(BLOCK_TIMES)):
            if BLOCK_TIMES[y] == timeFormatted:
                currentBlock = y + 1
                print("The block has changed !!! >> " + str(currentBlock))
                break
        if not currentBlock:
            print("A check has occured but failed")
        else:
            currentPeriod = block_to_period(currentBlock)
            if currentPeriod:
                print("\nThe period has changed !!! >> " + str(currentPeriod) + "\n")
                
                for userid in Linkdata.keys():

                    print("messaging this user >> " + str(userid))

                    classLink = Linkdata[userid][currentPeriod-1]

                    userprofile = await client.fetch_user(userid)
                    await userprofile.send("Join Your Class Here: " + classLink)
        await asyncio.sleep(interval)

@client.event
async def on_ready():
    print("Bot is ONLINE\n")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("ver 0.0.1"))
    client.loop.create_task(send_interval_message())

@client.event
async def on_message(message):
    args = message.content.split(' ')
    if(args[0] == ">create_profile"):
        await create_profile(message)
    elif(args[0] == '>set_link'):
        await set_link(message)
    elif(args[0] == '>delete_profile'):
        await delete_profile(message)
    elif(args[0] == '>am_pm_week'):
        await am_pm_week(message)
    #if(args[0] == '>test'):
        #await test(message)

client.run("Nzk5NzYyMzUzMjU1NDgxMzg0.YAISuw.SXOXjdmOd5qyzVUVWeA1c6Z4En4")


