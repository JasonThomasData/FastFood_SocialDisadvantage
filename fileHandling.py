import fiona 
import json

def getJsonData(fileName):
    with open(fileName, "r") as jsonDataFile:
        return json.load(jsonDataFile)

def saveJsonFile(fileName, jsonData):
    with open(fileName, "w") as jsonFile:
        jsonFile.write(json.dumps(jsonData))

