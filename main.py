import yaml
from user_scraper import *
from dm_scraper import *

with open("configuration.yaml", "r") as f: #Grab all the data from config file
    config = yaml.safe_load(f)
    


if config["mode"] == 1: # Grab EVERYTHING
    download_dms()
    download_all_servers()
elif config["mode"] == 2: #Grab all DMs
    download_dms()
elif config["mode"] == 3: #Grab all guilds
    download_all_servers()
elif config["mode"] == 4: #Grab entire guild
    download_guild(config['guildID'])
elif config["mode"] == 5: #Grab entire channel
    request = requests.get(url = f'''https://discord.com/api/v9/channels/{config['channelID']}''', headers= {"Authorization": config['authToken']})
    print(request.json())

    if request.json()["name"]: # If it has a name, use that, otherwise grab the DM recipient
        name = request.json()["name"]
        path = "json_output/channel_download/"
    else:
        name = request.json()["recipients"][0]["username"]
        path = "json_output/!direct_messages"


    download_channel(config['channelID'], path, name)
else:
    print("Mode must be number from 1-5. Please refer to configuration file")

