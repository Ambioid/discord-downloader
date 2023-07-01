import requests
import json
import time
import math
import os


requestLimit = 6
# Limit to how many requests per channel. Important because there is about
# 2 requests per second, but a single general channel could require 10,000 requests

requestWait = 0 # Wait time between every request being processed (seconds)

def download_channel(authToken, channelID, path, channelName, chunkLength):

    start_time = time.time()

    # sending get request and saving the response as response object
    request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit=100''', headers= {"Authorization": authToken})

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
    
    # If no error, just run until it has nothing left
    else:
        i = 1
        while (request.json()) and (i < requestLimit):
            
            # Counting progress
            print(f'''Request number: {i+2}, Messages: {(i+2)*100}, ''')
            i += 1

            # Grab id of last message to continue the chain
            msgid = request.json()[-1]["id"]

            fileName = f"""temp_chunk/chunk{math.ceil(i/chunkLength)}.json"""

            # GET new batch of messages
            request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit=100&before={msgid}''', headers= {"Authorization": authToken})
            
            if request.json():
                # Replace the json with new data
                with open(fileName, "a") as file:
                    # if json.dumps(request.json(), indent=4)[-1]:
                    file.write(json.dumps(request.json(), indent=4)[1:-2]+",")
            
            time.sleep(requestWait)
            

        print(f'''All data pulled, now merging chunks. Time: {round(time.time() - start_time, 2)}s''')

        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"""{path}{channelName}.json""", "w") as file:
            pass


        for i in range(math.ceil(i/chunkLength)):
            print("Currently merging Chunk number", i)
            with open(f"""temp_chunk/chunk{i+1}.json""", "r") as file:
                content = file.read()

            with open(f"""{path}{channelName}.json""", "a") as file:
                file.write(content)
            


        with open(f"""{path}{channelName}.json""", "r") as file:
            content = file.read()
        with open(f"""{path}{channelName}.json""", "w") as file:
            file.write(content[:-1]+"\n]")
        print("Everything merged, task Finished\n")


