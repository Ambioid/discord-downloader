import requests
import json
import time
import math
import os

def download_channel(channelID, path, channelName, authToken, chunkLength):

    start_time = time.time()

    # sending get request and saving the response as response object
    request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit=100''', headers= {"Authorization": authToken})

    # Inital paste of the content into the output file.
    with open("chunk1.json", "w") as file:
        content = file.write(json.dumps(request.json(), indent=4)[:-2]+",")

    # print(json.dumps(request.json(), indent=4))

    
    if ('message' in request.json()):
        print('message' in request.json(), request.json())
        if not os.path.exists(path):
            os.makedirs(path)

        with open(f"""{path}{channelName}.json""", "w") as file:
            file.write(json.dumps(request.json(), indent=4))

    else:
        i = 0
        while request.json():
            # Counting progress
            i += 1
            print(f'''Request number: {i+2}, Messages: {(i+2)*100}, ''')

            # Grab id of last message to continue the chain
            msgid = request.json()[-1]["id"]

            fileName = f"""chunk{math.ceil(i/chunkLength)}.json"""

            # GET new batch of messages
            request = requests.get(url = f'''https://discord.com/api/v9/channels/{channelID}/messages?limit=100&before={msgid}''', headers= {"Authorization": authToken})
            
            # Replace the json with new data
            with open(fileName, "a") as file:
                file.write(json.dumps(request.json(), indent=4)[1:-2]+",")


        print(f'''All data pulled, now merging chunks. Time: {round(time.time() - start_time, 2)}s''')

        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"""{path}{channelName}.json""", "w") as file:
            pass


        for i in range(math.ceil(i/chunkLength)):
            print("Currently merging Chunk number", i)
            with open(f"""chunk{i+1}.json""", "r") as file:
                content = file.read()

            with open(f"""{path}{channelName}.json""", "a") as file:
                file.write(content)
            


        with open(f"""{path}{channelName}.json""", "r") as file:
            content = file.read()
        with open(f"""{path}{channelName}.json""", "w") as file:
            file.write(content[:-1]+"\n]")
        print("Everything merged, task Finished\n")



