import json
import os
import urllib.request


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

pathToFile = dir_path + "\\awslinks.json"
print(pathToFile)

with open(pathToFile, 'r') as infile:
    links = json.load(infile)
    for i in links["links"]:  
        name = i[-8:]
        urllib.request.urlretrieve(i, name)


       