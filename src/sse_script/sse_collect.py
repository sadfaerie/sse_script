#!/usr/bin/env python3

import json
from sseclient import SSEClient
import requests
import pymongo

from constants import * 

def main():
    """ Consumes URL data and persists it to mongodb. """

    mongo_client = pymongo.MongoClient(MONGO_HOST, 27017)

    db = mongo_client.pymongo_sse
    sse_client = SSEClient(requests.get(URL, stream=True))
    db_events = db.events

    try:
        print("\033[1mInserting results to database. Press Ctrl+C to abort.\033[0m")
        for event in sse_client.events():
            result = db_events.insert_one(json.loads(event.data))

    except KeyboardInterrupt:
        mongo_client.close()
        print("Inserting interrupted. Aborting.")


if __name__ == "__main__":
    main()