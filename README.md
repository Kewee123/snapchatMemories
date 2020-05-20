# snapchatMemories
Download all snapchat memories from your snapchat account data.
Use Case:
    I wanted to save all my snapchat memories without clicking month by month and downloading in the app nor clicking the download link one by one in the file that snapchat returns when you ask for your data.

## Requirements
If you don't have the following programs, install it first.
-Python 3.8
-https://www.python.org/downloads/release/python-380/

Modules
-Requests
`pip install requests` (python should have installed pip already)

If it throws any other errors, then you would probably have to pip install it as well.

Run in Windows for now, will make the path change for unix sometime soon.
Also, the metadata per file isn't changed yet, so that will be added sometime later.
## Steps

### Step 1
Request and download data from snapchat
https://support.snapchat.com/en-US/a/download-my-data


### Step 2
Place memories_history.json folder into same folder as convertMemories.py

Run convertMemories.py

`py convertMemories.py`

It will create a file called convertedMemories.json

### Step 3
Run convert.py

`py convert.py`

It will grab all the links from convertedMemories.json and turn them into links that the downloadFiles.py can download
The output will be aws_links.json and it will print 

### Step 4
Run downloadFiles.py

`py downloadFiles.py`

It will then start to download all the files in your snapchat_memories and dump them into the same folder.
The files are labelled by their date and time.