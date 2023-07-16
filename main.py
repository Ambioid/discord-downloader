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
    download_channel(config['channelID'], "json_output/channel_download/", request.json()["name"])
else:
    print("Mode must be number from 1-5. Please refer to configuration file")

