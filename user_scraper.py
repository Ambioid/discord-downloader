import requests
from guild_scraper import *


def download_all_servers():
    with open("configuration.yaml", "r") as f: #Grab all the data from config file
        config = yaml.safe_load(f)

    request = requests.get(url = f'''https://discord.com/api/v9/users/@me/guilds''', headers= {"Authorization": config['authToken']})

    for i in range(len(request.json())):
        print(request.json()[i]["id"], request.json()[i]["name"])
        
        
        download_guild(request.json()[i]["id"])
        time.sleep(config['serverWait']*random.uniform(1-config["waitVariation"], 1+config["waitVariation"]))

        

    print("User's information downloaded")