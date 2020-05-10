# snapchatMemories
Download all snapchat memories from your snapchat account
I wanted to save them to my google photos and realized that there was no easy way to get all of them at once.

## Steps
Request and download data from snapchat
https://support.snapchat.com/en-US/a/download-my-data

### Step 2
Place memories_history.json folder into same folder as convertMemories.py
Run convertMemories.py
It will create a file called convertedMemories.json

### Step 3
Run the convert.py
It will grab all the links from convertedMemories.json and turn them into links that the downloadFiles.py can download

### Step 4
Run downloadFiles.py
It will  then start to download all the files in your snapchat_memories and dump them into the folder.