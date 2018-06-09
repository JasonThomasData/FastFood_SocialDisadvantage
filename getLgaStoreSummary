#!/usr/bin/env python3

import fiona
import json
from shapely.geometry import Point, MultiPolygon, Polygon, asShape
from fileHandling import getJsonData, getShapeData, saveJsonFile 

def checkShapeContainsPoint(polygon, point):
    shape = asShape(polygon)
    if shape.contains(point):
        return True
    return False

def checkPolygonContainsLngLat(polygon, lngLat):
    if lngLat is None:
        return False
    point = Point(lngLat[0], lngLat[1])
    return checkShapeContainsPoint(polygon, point)

def getMultiPolygon(coordinatesList):
    createdPolygons = []
    for coordinates in coordinatesList:
        polygon = Polygon(coordinates[0])
        createdPolygons.append(polygon)
    multiPolygon = MultiPolygon(polygons=createdPolygons)
    return multiPolygon

def getPolygonByType(coordinates, polygonType):
    if geometryType == "MultiPolygon":
        polygon = getMultiPolygon(coordinates)
    else:
        polygon = Polygon(coordinates[0])
    return polygon

def removePlacedPoints(allStoresData, indexesOfPlacedPoints):
    """
    Best to iterate backwards so that index to be deleted isn't shifted.
    """
    for i in reversed(indexesOfPlacedPoints):
        del allStoresData[i]

def giveUserStatus(lgaData, allStoresData):
    print("Data for {} {}".format(lgaData["lgaCode"], lgaData["lgaName"]))
    print("{} stores in this lga".format(lgaData["stores"]))
    print("{} points to check".format(len(allStoresData)))

def summariseStoresWithinShape(allStoresData, lgaData, polygon):
    lgaStoreCount = 0
    indexesOfPlacedPoints = []
    for i, storeData in enumerate(allStoresData):
        storeName = storeData["store"]
        storeLngLat = storeData["lngLat"]
        if checkPolygonContainsLngLat(polygon, storeLngLat):
            indexesOfPlacedPoints.append(i)
            lgaData[storeName] += 1
    removePlacedPoints(allStoresData, indexesOfPlacedPoints)

def getTotalStoresForLga(lgaData):
    total = lgaData["Hungry Jacks"] + lgaData["KFC"] + lgaData["McDonalds"] + lgaData["Red Rooster"]
    lgaData["stores"] = total

def addToLgaStoreSummary(lgaStoreSummary, lgaData):
    lgaStoreSummary.append(lgaData)

if __name__ == "__main__":
    allStoresData = getJsonData("data/allStoresLngLat.json")
    shapeData = getShapeData("data/LGA_2016_AUST.shp")
    lgaStoreSummary = []

    for shape in shapeData:
        lgaData = {
            "lgaName" : shape["properties"]["LGA_NAME16"],
            "lgaCode" : shape["properties"]["LGA_CODE16"],
            "Hungry Jacks" : 0,
            "KFC" : 0,
            "McDonalds" : 0,
            "Red Rooster" : 0,
            "stores" : 0
        }

        geometry = shape["geometry"]
        if geometry is None:
            continue

        coordinates = geometry["coordinates"]
        geometryType = geometry["type"]

        polygon = getPolygonByType(coordinates, geometryType)

        summariseStoresWithinShape(allStoresData, lgaData, polygon)
        getTotalStoresForLga(lgaData)
        addToLgaStoreSummary(lgaStoreSummary, lgaData)

        giveUserStatus(lgaData, allStoresData)

    saveJsonFile("data/lgaStoreSummary.json", lgaStoreSummary)

