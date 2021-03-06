#!/usr/bin/env python3

from fileHandling import getJsonData

def getTotalStoreSummary(lgaStoreSummary):
    totalStoreCount = 0
    for lngLat in lgaStoreSummary:
        totalStoreCount += lngLat["stores"]
    return totalStoreCount

def getTotalNullLngLat(allStoresLngLat):
    totalNullCount = 0
    for lngLat in allStoresLngLat:
        if lngLat is None:
            totalNullCount += 1
    return totalNullCount

if __name__ == "__main__":
    allStoresLngLatFilename = "data/allStoresLngLat.json"
    lgaStoresSummaryFilename = "data/lgaStoreSummary.json"

    allStoresLngLat = getJsonData(allStoresLngLatFilename)
    lgaStoreSummary = getJsonData(lgaStoresSummaryFilename)

    totalLngLat = len(allStoresLngLat)
    totalNullLngLat = getTotalNullLngLat(allStoresLngLat)
    totalStoreSummary = getTotalStoreSummary(lgaStoreSummary)

    print("There are {} store lng,lat coords in {}".format(totalLngLat, allStoresLngLatFilename))
    print("There are {} null lng,lat coords in {}".format(totalNullLngLat, allStoresLngLatFilename))
    print("There are {} stores in {} placed in LGAs".format(totalStoreSummary, lgaStoresSummaryFilename))

