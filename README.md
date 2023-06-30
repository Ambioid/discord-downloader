# discord-scraper
A python script I wrote that will download entire contents of a discord channel through many HTTPS calls. Chances are, your discord server won't be around forever, so this tool can provide a way to archive and store old chatlogs to preserve the past. Though the json file does get quite big if there's a lot of messages, so handle with care.

# Warning:
Selfhosted bots are against discord's terms of service, and may lead to termination of account. By using this you understand and accept such risk.

# How to use
<Insert description here>


## todo:
- [x] Send HTTPS requests
- [x] Authorization token
- [x] Store requests
- [x] Combine multiple outputs (Breakthrough was the knowledge that json is a list of dicts)
- [x] Continue from last request (Get the msg ID and do before=id)
- [x] Iterate until the entire channel is stored
- [x] Improve performance (Chunk together files and merge at end)
- [x] Output file named after all the channel.
- [ ] Centralize config in a configuration file
- [ ] Add guild data as well while we've got it
- [ ] Better way to grab auth token
- [x] Make it get all the channels for a server
- [x] Make it get all servers for a user
- [ ] Same with all DMs/friends?
- [ ] Option to download images
- [ ] A secondary program to synthesize and distill the information in a more readable way


Things to do before git pushing: 
1. Delete all authorization tokens and IDs
2. Delete the chunks
3. Delete the stuff in json_output.