import requests
import json
import time
import math
import os
import yaml
import random
# Oh my god there are so many imports


def download_channel(channelID, path, channelName):
    with open("configuration.yaml", "r") as f: #Grab all the data from config file
        config = yaml.safe_load(f)

    start_time = time.time()

    # sending get request and saving the response as response object
    request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit={config["requestLength"]}''', headers= {"Authorization": config['authToken']})

    # Inital paste of the content into the temp output file.
    with open("temp_chunk/chunk1.json", "w") as file:
        content = file.write(json.dumps(request.json(), indent=4)[:-2]+",")

    # If error message, dump the error message into the output instead
    if ('message' in request.json()):
        print('message' in request.json(), request.json())
        if not os.path.exists(path):
            os.makedirs(path)

        with open(f"""{path}{channelName}.json""", "w") as file:
            file.write(json.dumps(request.json(), indent=4))
    
    # If no error message, just run until it has nothing left
    else:
        i = 1
        while (request.json()) and (i < config["requestLimit"]):
            
            # Counting progress
            print(f'''Request number: {i+2}, Messages: {(i+2)*config["requestLength"]}, ''')
            i += 1

            # Grab id of last message to continue the chain
            msgid = request.json()[-1]["id"]

            fileName = f"""temp_chunk/chunk{math.ceil(i/config["chunkLength"])}.json"""

            # GET new batch of messages
            request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit={config["requestLength"]}&before={msgid}''', headers= {"Authorization": config['authToken']})
            
            if request.json():
                # Replace the json with new data
                with open(fileName, "a") as file:
                    file.write(json.dumps(request.json(), indent=4)[1:-2]+",")
            
            time.sleep(config["requestWait"]*random.uniform(1-config["waitVariation"], 1+config["waitVariation"]))
            

        print(f'''All data pulled, now merging chunks. Time: {round(time.time() - start_time, 2)}s''')

        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"""{path}{channelName}.json""", "w") as file:
            pass

        # Go through all the chunks and just merge the remaining information
        for i in range(math.ceil(i/config["chunkLength"])):
            print("Currently merging Chunk number", i)
            with open(f"""temp_chunk/chunk{i+1}.json""", "r") as file:
                content = file.read()

            with open(f"""{path}{channelName}.json""", "a") as file:
                file.write(content)

        # Just clean up, clip the comma off the back
        with open(f"""{path}{channelName}.json""", "r") as file:
            content = file.read()
        with open(f"""{path}{channelName}.json""", "w") as file:
            file.write(content[:-1]+"\n]")

# This is not the way I intended on doing it at all originally, my 1st design of the program
# actually involved me reading the file's contents and organically adding new entries to the
# .json file as a list of dicts but the merging process made it take exponentially longer, so
# instead I just repeatedly appended the new chunk information with a comma, then snipped 
# the comma off at the end. Didn't have chunks originally but found that using chunks speeds it up.
        
        print("Everything merged, task Finished\n")


