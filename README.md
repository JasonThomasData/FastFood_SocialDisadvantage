# Fast food and social disadvantage

This is some research I wanted to do regarding fast food and social disadvantage.

Steps to reproduce:

    ./collectRestaurantData.sh
    ./combineRestaurantData.py
    follow manual steps in collectABSData.md
    ./getLgaStoreSummary.py #This part is very slow, would be good to make it faster
    ./checkSums.py

For the rest, do:
    - import SEIFA csv as dataframe
    - import lgaStoreSummary json as dataframe
    - inner join the dataframes on matching Lga names
    - check the length of the dataframe is the same as the lgaStoreSummary datafile

Questions about data
- Is SEIFA an indication that communities are more likely to face poverty?
- Are people currently less or more likely to be buying takeaway food? Are they more likely to buy food close to them?
- Are the data of restaurants exhaustive, or are there stores that are not on the maps?
- Is comparing SIEFA to restaurants per population a good statistic? Is this a significant correlation?