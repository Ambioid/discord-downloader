import requests
from scraper import *

authToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Insert your own authorization token (DO NOT SHARE WITH OTHERS)

guildID = "XXXXXXXXXXXXXXXXXX"

chunkLength = 500

request = requests.get(url = f'''https://discord.com/api/v9/guilds/{guildID}/channels''', headers= {"Authorization": authToken})
category = ""

for i in range(len(request.json())):
    print(request.json()[i]["id"], request.json()[i]["name"], request.json()[i]["type"])
    
    if request.json()[i]["type"] == 4:
        category = request.json()[i]["name"]
        print("Category, now skipping")
    else:
        download_channel(request.json()[i]["id"], f'''json-output/{category}/''', {request.json()[i]["name"]}, authToken, chunkLength)


