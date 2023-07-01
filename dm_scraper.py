import requests
from channel_scraper import *


def download_dms():
    with open("configuration.yaml", "r") as f: #Grab all the data from config file
            config = yaml.safe_load(f)

    request = requests.get(url = f'''https://discord.com/api/v9/users/@me/channels''', headers= {"Authorization": config["authToken"]})

    print(request.json())
    for i in range(len(request.json())):

        with open("configuration.yaml", "r") as f: #Grab all the data from config file
            config = yaml.safe_load(f)

        # If normal DM, just make the name the filename
        if request.json()[i]["type"] == 1:
            print("DM:", request.json()[i]["id"], request.json()[i]["recipients"][0]["username"])
            name = request.json()[i]["recipients"][0]["username"]

        # If group DM, add the name of everyone in it 
        elif request.json()[i]["type"] == 3:
            name = "Group DM: "
            for recipient in request.json()[i]["recipients"]:
                print(recipient["username"])
                name += recipient["username"]+", "
            name = name[:-2]

        
        download_channel(request.json()[i]["id"], f'''json_output/!direct_messages/''', name)
        
        time.sleep(config["channelWait"]*random.uniform(1-config["waitVariation"], 1+config["waitVariation"]))

        
    print(request)
    print("User's information downloaded")