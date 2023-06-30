import requests
from guild_scraper import *

authToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Insert your own authorization token (DO NOT SHARE WITH OTHERS)

request = requests.get(url = f'''https://discord.com/api/v9/users/@me/guilds''', headers= {"Authorization": authToken})

chunkLength = 500

serverWait = 0 # Wait time between each server (seconds)


for i in range(len(request.json())):
    print(request.json()[i]["id"], request.json()[i]["name"])
    
    
    download_guild(authToken, request.json()[i]["id"], request.json()[i]["name"], chunkLength)
    time.sleep(serverWait)

    

print("User's information downloaded")