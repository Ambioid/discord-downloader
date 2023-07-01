import requests
from channel_scraper import *


# chunkLength = 500


def download_guild(guildID):
    with open("configuration.yaml", "r") as f: #Grab all the data from config file
        config = yaml.safe_load(f)

    # Find all the channels in a guild
    request = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}/channels''', headers= {"Authorization": config['authToken']})

    # Grab guild info
    info = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}''', headers= {"Authorization": config['authToken']}).json()
    guildName = info["name"]
    category = ""
    
    for i in range(len(request.json())):
        print(request.json()[i]["id"], request.json()[i]["name"], request.json()[i]["type"])
        
        #I'm pretty sure this only finds the right category sometimes, might be a bug
        if request.json()[i]["type"] == 4: 
            category = request.json()[i]["name"].replace("/", "\/") 
            print("Category, now skipping")
        
        # Go through all the channels in a server and start downloading
        else:
            if not os.path.exists(f'''json_output/{guildName.replace("/", "∕")}/'''):
                os.makedirs(f'''json_output/{guildName.replace("/", "∕")}/''')
            
            with open(f"""json_output/{guildName.replace("/", "∕")}/info.json""", "w") as file:
                file.write(json.dumps(info, indent=4))

            download_channel(request.json()[i]["id"], f'''json_output/{guildName.replace("/", "∕")}/{category.replace("/", "∕")}/''', request.json()[i]["name"].replace("/", "∕"))

    print("Server downloaded")
