import json
import datetime
import random

ROLE_VOLUNTEER = 811698025600122942
GUILD_ID = 799773078557163541

LINKDATA_FILE = 'link_data.json'
LOG_FILE_DIR = 'log.txt'

BLOCK_TIMES = ["07:57", "08:57", "09:57", "10:57", "13:07", "13:52"]
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

ADMIN_COMMAND_LOG_TYPE = "Admin Command"
ADMIN_SUPPORTED_VARIABLES = locals()

MAX_INT = 10000

am_pm_week = 0
is_enabled = True

colors = [0xff62ff, 0x95ff00, 0x00d5ff, 0xe89816, 0xaa8be7, 0x04a979, 0xFF6978, 0x3774EE, 0xecf9de, 0x23AA33, 0xA88C00, 0x7F0000]
colors_rarity = [1, 5, 10, 50, 90, 200, 500, 1000, 2000, 5000, 7500, 10000]

def update_link_data(func, *args):
    async def wrapper_update_link_data(method, *args):
        await func(method, args)
        edit_link_data()
    return wrapper_update_link_data

def read_link_data():
    with open(LINKDATA_FILE) as json_file:
        link_data_json = json_file.read()
        link_data = json.loads(link_data_json)
        return link_data

link_data = read_link_data()

def edit_link_data():
    with open(LINKDATA_FILE, 'w+') as json_file:
        json_file.write(json.dumps(link_data, indent=4))
        # json.dump(link_data, indent=4)

def block_to_period(block):
    time_week_day = datetime.datetime.now().strftime("%w")
    if(time_week_day == 0 or time_week_day == 6):
        return 
    try:
        return BLOCK_PERIOD_DATA[am_pm_week][int(time_week_day)-1][block-1]
    except:
        print_log("Error/block_to_period", f"Error that shouldn't be possible has occured... Day of the week is {time_week_day}")

async def check_for_role(client, role, userid):
    server = client.get_guild(GUILD_ID)
    user_member = await server.fetch_member(userid)
    for user_role in user_member.roles:
        if(user_role.id == role):
            return True
    return False

def get_discord_key():
    with open('discord_key.txt', 'r') as discord_key_file:
        return discord_key_file.read()

def print_log(log_type, log_message):
    print(f"[{datetime.datetime.now().strftime('%x')} | {datetime.datetime.now().strftime('%X')}] [{log_type}]: {log_message}")

    log_file = open(LOG_FILE_DIR, "a")
    log_file.write(f"[{datetime.datetime.now().strftime('%x')} | {datetime.datetime.now().strftime('%X')}] [{log_type}]: {log_message}\n")
    log_file.close()

def get_color():
    random_int = random.randint(1,MAX_INT)
    for i in range(len(colors_rarity)):
        if(random_int < colors_rarity[i]):
            return colors[i]