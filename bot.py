import os
import discord
import datetime
import time
import asyncio
 
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

blocktimes = ["7:55", "9:00", "10:00", "11:00", "13:10", "13:55"]
blockperioddata = [ 
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

ampmweek = 0

def block_to_period(block):
    timeweekday = timeNow.datetime.now().strftime("%w")
    try:
        return blockperioddata[ampmweek][int(timeweekday)][block-1]
    except:
        print("\nThe day number is >>" + str(int(timeweekday)-1))
        return

async def send_interval_message():
    await client.wait_until_ready()
    interval = 15
    while not client.is_closed():

        timeFormated = timeNow.datetime.now().strftime("%H:%M")

        currentBlock = -1

        for y in range(len(blocktimes)):

            if blocktimes[y] == timeFormated:
                currentBlock = y + 1
                print("The block has changed !!! >> " + str(currentBlock))

        if currentBlock != -1:

            currentPeriod = block_to_period(currentBlock)
            print("\nThe period has changed !!! >> " + str(currentPeriod) + "\n")
            
            for x in range(len(Classtime[currentPeriod-1])):

                userid = Classtime[currentPeriod-1][x]
                print("messaging this user >> " + str(userid))

                idperiod = userid.split("|")

                classLink = Linkdata[int(idperiod[0])][int(idperiod[1])-1]
                userprofile = await client.fetch_user(int(idperiod[0]))
                await userprofile.send("Join Your Class Here: " + classLink)

                #channel = client.get_channel(800439342626897920)
                #await channel.send(Linkdata[int(idperiod[0])][int(idperiod[1])])
            
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

    if(message.content.startswith('>setlink')):

        try:

            Linkdata[message.author.id].append(args[1])

        except:

            print("\nCreating a new Profile... ", message.author)

            Linkdata[message.author.id] = [[],[],[],[],[],[],[],[]]
            Linkdata[message.author.id][int(args[2])-1] = args[1]

        try:

            Classtime[int(args[2])-1].append(str(message.author.id) + "|" + args[2])

        except:
            print("an error has happened")
            #Classtime[args[2]]=[]
            #Classtime[args[2]].append(str(message.author.id) + "|" + str(args[2]))

        print("All Link Information >> ", Linkdata)
        print("All Classtime Infromation >> ", Classtime, "\n")

        await message.reply("Added link for " + str(message.author))

    if(message.content.startswith('>sendDM')):

        await message.author.send('BRUH')

    if(message.content.startswith('>deleteprofile')):

        del Linkdata[message.author.id]
        await message.reply(str(message.author.id) + "'s profile has been deleted")

        for y in range(len(Classtime)):
            try:
                Classtime[y].remove(str(message.author.id) + "|" + str(y+1))
            except:
                pass

client.run("Nzk5NzYyMzUzMjU1NDgxMzg0.YAISuw.SXOXjdmOd5qyzVUVWeA1c6Z4En4")
 

