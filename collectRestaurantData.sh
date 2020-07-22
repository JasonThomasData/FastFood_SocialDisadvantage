#!/usr/bin/env bash

# Found by looking at restaurant's main map script
curl https://www.kfc.com.au/find-store-all -o data/kfc.json

# Found by looking at restaurant's main map script
curl https://mcdonalds.com.au/data/store -o data/mcdonalds.json

# Found by looking at restaurant's main map script
curl https://www.redrooster.com.au/api/stores/3/ -o data/redRooster.json

# Found by looking at restaurant's network traffic
curl https://www.hungryjacks.com.au/api/storelist -o data/hungryJacks.json
