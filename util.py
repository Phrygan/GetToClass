import json
import datetime

ROLE_VOLUNTEER = 811698025600122942
GUILD_ID = 799773078557163541

LINKDATA_FILE = 'link_data.json'
LOG_FILE_DIR = 'log.txt'

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

ADMIN_COMMAND_LOG_TYPE = "Admin Command"
ADMIN_SUPPORTED_VARIABLES = locals()

am_pm_week = 0

def update_link_data(func):
    def wrapper_update_link_data():
        func()
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
    if(time_week_day == 5 or time_week_day == 6):
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

def print_log(log_type, log_message):
    print(f"[{datetime.datetime.now().strftime('%x')} | {datetime.datetime.now().strftime('%X')}] [{log_type}]: {log_message}")

    log_file = open(LOG_FILE_DIR, "a")
    log_file.write(f"[{datetime.datetime.now().strftime('%x')} | {datetime.datetime.now().strftime('%X')}] [{log_type}]: {log_message}\n")
    log_file.close()