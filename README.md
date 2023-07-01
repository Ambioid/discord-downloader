# Discord Downloader
A python script I wrote that will download entire contents of a discord channel through many HTTPS calls. Chances are, your discord server won't be around forever, so this tool can provide a way to archive and store old chatlogs to preserve the past. Though the json file does get quite big if there's a lot of messages, so handle with care.

# Warning:
Selfhosted bots are against discord's terms of service, and may lead to termination of account. By using this you understand and accept such risk.

# How to use
1. Grab your authenticatin token for your discord account (open inspect in browser, go to network, click on any GET request, scroll down and in the headers section one of them should be an auth token)
2. Paste it into the program, as well as filling in the other necessary details in the configuration.yaml
3. You can also make some changes to the other settings in the configuration.yaml file
4. Run main.py and it should function


## What I've learned:
This has been a good lesson in how HTTPS requests and APIs work, how to manage jsons and read/write data, good for learning to subdivide programs into multiple files, and also for how configuration files work.

## Features:
- [x] Send HTTPS requests
- [x] Authorization token
- [x] Store requests
- [x] Combine multiple outputs (Breakthrough was the knowledge that json is a list of dicts)
- [x] Continue from last request (Get the msg ID and do before=id)
- [x] Iterate until the entire channel is stored
- [x] Improve performance (Chunk together files and merge at end)
- [x] Output file named after all the channel.
- [x] Centralize config in a configuration file
- [x] Add guild data as well while we've got it
- [ ] Better way to grab auth token
- [x] Make it get all the channels for a server
- [x] Make it get all servers for a user
- [x] Same with all DMs/friends?
- [ ] Option to download images
- [ ] A secondary program to synthesize and distill the information in a more readable way
- [x] Finish this and move on with my life


Things to do before git pushing: 
1. Delete all authorization tokens and IDs
2. Delete the chunks
3. Delete the stuff in json_output.

