#!/usr/bin/env python3

import json
from fileHandling import getJsonData, saveJsonFile

def getHungryJacksLngLat(data):
    return {
        "store": "Hungry Jacks",
        "lngLat": [float(data["location"]["long"]), float(data["location"]["lat"])]
    }

def getKfcLngLat(data):
    return {
        "store": "KFC",
        "lngLat": [float(data["lng"]), float(data["lat"])]
    }

def getMcdonaldsLngLat(data):
    lngLat = data["store_geocode"].split(',')
    return {
        "store": "McDonalds",
        "lngLat": [float(lngLat[0]), float(lngLat[1])]
    }

def getRedRoosterLngLat(data):
    try:
        return {
            "store": "Red Rooster",
            "lngLat": [float(data["longitude"]), float(data["latitude"])]
        }
    except TypeError:
        return None

def addLngLatIfNotNone(lngLatData, lngLatDatum):
    if lngLatData is not None:
        lngLatDatum.append(lngLatData)

def getLngLat(rawDatum, callback):
    lngLatDatum = []
    for rawData in rawDatum:
        lngLatData = callback(rawData)
        addLngLatIfNotNone(lngLatData, lngLatDatum)
    return lngLatDatum

if __name__ == "__main__":
    hungryJacksDatum = getJsonData("data/hungryJacks.json")
    kfcDatum = getJsonData("data/kfc.json")
    mcdonaldsDatum = getJsonData("data/mcdonalds.json")
    redRoosterDatum = getJsonData("data/redRooster.json")

    hungryJacksLngLat = getLngLat(hungryJacksDatum, getHungryJacksLngLat)
    kfcLngLat = getLngLat(kfcDatum, getKfcLngLat)
    mcdonaldsLngLat = getLngLat(mcdonaldsDatum, getMcdonaldsLngLat)
    redRoosterLngLat = getLngLat(redRoosterDatum, getRedRoosterLngLat)

    allStoresLngLat = hungryJacksLngLat + kfcLngLat + mcdonaldsLngLat + redRoosterLngLat

    saveJsonFile("data/allStoresLngLat.json", allStoresLngLat)

