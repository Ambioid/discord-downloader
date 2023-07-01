import requests
from channel_scraper import *

authToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Insert your own authorization token (DO NOT SHARE WITH OTHERS)

request = requests.get(url = f'''https://discord.com/api/v9/users/@me/channels''', headers= {"Authorization": authToken})

chunkLength = 500

serverWait = 0 # Wait time between each server (seconds)

print(request.json())
for i in range(len(request.json())):

    # If normal DM or group DM, give different naming scheme
    if request.json()[i]["type"] == 1:
        print("DM:", request.json()[i]["id"], request.json()[i]["recipients"][0]["username"])
        name = request.json()[i]["recipients"][0]["username"]

    elif request.json()[i]["type"] == 3:
        name = "Group DM: "
        for recipient in request.json()[i]["recipients"]:
            print(recipient["username"])
            name += recipient["username"]+", "
        name = name[:-2]

    
    download_channel(authToken, request.json()[i]["id"], f'''json_output/!direct_messages/''', name, chunkLength)
    
    time.sleep(serverWait)

    
print(request)
print("User's information downloaded")