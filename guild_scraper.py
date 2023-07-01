import requests
from channel_scraper import *

# authToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Insert your own authorization token (DO NOT SHARE WITH OTHERS)
# guildID = "XXXXXXXXXXXXXXXXXX"

# chunkLength = 500

channelDelay = 0 # Wait time (seconds) between each channel

def download_guild(authToken, guildID, chunkLength):
    request = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}/channels''', headers= {"Authorization": authToken})
    category = ""

    info = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}''', headers= {"Authorization": authToken}).json()
    guildName = info["name"]
    for i in range(len(request.json())):
        print(request.json()[i]["id"], request.json()[i]["name"], request.json()[i]["type"])
        # channelName = request.json()[i]["name"]
        

        if request.json()[i]["type"] == 4:
            category = request.json()[i]["name"].replace("/", "\/")
            print("Category, now skipping")
        else:

            if not os.path.exists(f'''json_output/{guildName.replace("/", "∕")}/'''):
                os.makedirs(f'''json_output/{guildName.replace("/", "∕")}/''')
            
            with open(f"""json_output/{guildName.replace("/", "∕")}/info.json""", "w") as file:
                file.write(json.dumps(info, indent=4))

            download_channel(authToken, request.json()[i]["id"], f'''json_output/{guildName.replace("/", "∕")}/{category.replace("/", "∕")}/''', request.json()[i]["name"].replace("/", "∕"), chunkLength)
            time.sleep(channelDelay)

print("Guild downloaded")
