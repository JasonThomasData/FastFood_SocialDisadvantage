# Fast food and social disadvantage

This is some research I wanted to do regarding fast food and social disadvantage.

Steps to reproduce:

    ./collectRestaurantData
    ./combineRestaurantData
    #collectABSData.md (Manual steps)
    ./getLgaStoreSummary
    ./checkSums

For the rest, do:
    - import SEIFA csv as dataframe
    - import lgaStoreSummary json as dataframe
    - inner join the dataframes on matching Lga names
    - check the length of the dataframe is the same as the lgaStoreSummary datafile

