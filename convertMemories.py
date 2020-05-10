import json
import os
import urllib.request
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

pathToFile = dir_path + "\\memories_history.json"
print(pathToFile)

newCreation = defaultdict(dict)
with open(pathToFile, 'r') as infile:
    jsonFile = json.load(infile)
    for i in jsonFile["Saved Media"]:  
        date = i["Date"] 
        downloadLink = i["Download Link"]
        dataType = i["Media Type"]
        print("\n")
        newCreation[date]["link"] = downloadLink
        newCreation[date]["type"] = dataType
for i in newCreation:
    print(i)
    print(newCreation[i]["link"])
    print(newCreation[i]["type"])
    print("\n")

with open('convertedMemories.json', 'w') as outfile:
    json.dump(newCreation, outfile)