import fiona
import pandas
import json

def getJsonData(fileName):
    with open(fileName, "r") as jsonDataFile:
        return json.load(jsonDataFile)

def getShapeData(fileName):
    return fiona.open(fileName)

def getCsvDataFrame(fileName):
    return pandas.read_csv(fileName)

def getJsonDataFrame(fileName):
    jsonData = getJsonData(fileName)
    return pandas.DataFrame(jsonData, index=[0])

def saveJsonFile(fileName, jsonData):
    with open(fileName, "w") as jsonFile:
        jsonFile.write(json.dumps(jsonData))
