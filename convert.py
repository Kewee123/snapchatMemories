
import json
import requests
import threading
import concurrent.futures
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path = dir_path + "\\convertedMemories.json"
with open(dir_path, 'r') as f:
    data = json.load(f)

""" rawLinks={}
rawType=[]

for d in data:
    rawLinks[d] = data[d]["link"]
    rawType.append(data[d]["type"])

print(rawType) """

def geturl(rawlink: str, date: str, dataType: str):
    r = requests.post(rawlink)
    returnDict = {}
    returnDict[0] = {date, r.text, dataType}
    return list(returnDict.values())

links = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = {}
    for date in data:
        futures[date] = executor.submit(geturl, data[date]["link"], date, data[date]["type"])

    for future in concurrent.futures.as_completed(futures.values()):
        try:
            result = future.result()
            links.append(result)
            """ print(result) """
        except Exception:
            print(f"Exception when processing result {futures[future]}")

""" print(links) """

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

for i in links:
    print(i)
with open('aws_links.json', 'w') as f:
    json.dump(links, f, default=set_default)