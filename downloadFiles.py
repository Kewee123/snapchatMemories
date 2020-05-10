import json
import os
import urllib.request


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

pathToFile = dir_path + "\\aws_links.json"
print(pathToFile)

with open(pathToFile, 'r') as infile:
    links = json.load(infile)
    for i in links:  
        date = i["date"]
        dataType = i["type"]
        link = i["link"]
        
        name = date.replace(":", "")
        if(dataType == "PHOTO"):
            name+=".jpg"
        else:
            name+=".mp4"

        urllib.request.urlretrieve(link, name)


       