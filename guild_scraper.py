import requests
from channel_scraper import *

# authToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Insert your own authorization token (DO NOT SHARE WITH OTHERS)
# guildID = "XXXXXXXXXXXXXXXXXX"

# chunkLength = 500

channelDelay = 0 # Wait time (seconds) between each channel

def download_guild(authToken, guildID, guildName, chunkLength):
    request = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}/channels''', headers= {"Authorization": authToken})
    category = ""

    for i in range(len(request.json())):
        print(request.json()[i]["id"], request.json()[i]["name"], request.json()[i]["type"])
        # channelName = request.json()[i]["name"]

        if request.json()[i]["type"] == 4:
            category = request.json()[i]["name"].replace("/", "\/")
            print("Category, now skipping")
        else:
            download_channel(authToken, request.json()[i]["id"], f'''json_output/{guildName.replace("/", "∕")}/{category.replace("/", "∕")}/''', request.json()[i]["name"].replace("/", "∕"), chunkLength)
            time.sleep(channelDelay)

print("Guild downloaded")