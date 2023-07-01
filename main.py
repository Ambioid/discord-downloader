import yaml
from user_scraper import *
from dm_scraper import *

with open("configuration.yaml", "r") as f: #Grab all the data from config file
    config = yaml.safe_load(f)
    


if config["mode"] == 1:
    download_dms()
    download_all_servers()
elif config["mode"] == 2:
    download_dms()
elif config["mode"] == 3:
    download_all_servers()
elif config["mode"] == 4:
    download_guild(config['guildID'])
elif config["mode"] == 5:
    request = requests.get(url = f'''https://discord.com/api/v9/guilds/{config['guildID']}/channels''', headers= {"Authorization": config['authToken']})
    download_channel(config['channelID'], "channel_download/", request.json()[0]["name"])
else:
    print("Mode must be number from 1-5. Please refer to configuration file")

