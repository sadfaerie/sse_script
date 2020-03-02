```
 ____            ___                        
/ ___| ___  ___ / _ \ _   _  ___ _ __ _   _ 
\___ \/ __|/ _ \ | | | | | |/ _ \ '__| | | |
 ___) \__ \  __/ |_| | |_| |  __/ |  | |_| |
|____/|___/\___|\__\_\\__,_|\___|_|   \__, |
                                      |___/ 
```
                                                      
CLI for collecting the SSE data, storing it in MongoDB and querying the results.

This script uses `SSEClient for Python` https://pypi.org/project/sseclient-py/ to iterate over http Server Sent Event (SSE) streams.
It then writes the events to MongoDB where the data can be queried using a simple CLI menu. 

The script consists of two modules:
- `sse_collect.py` that runs in the background and continuously writes events to the collection. 
- `sse_query.py` that provides a CLI interface for querying the data.


TO RUN THE SCRIPT LOCALLY
-------------------------
1. Make sure `pip` and `pipenv` is installed
2. Make sure `docker` is installed
3. Clone the repository and navigate to repository directory
4. Run `make install` to fetch dependencies
5. Activate Python virtualenv `pipenv shell`
6. Run `make run-mongo` to start mongodb docker container
7. run `make` to start the script
 
TO RUN THE SCRIPT IN A DOCKER CONTAINER
--------------------------------------- 
1. Clone the repository and navigate to repository directory
2. Run `docker-compose build` to build containers
3. Run `docker-compose up -d` to run containers in the background
4. Run `docker-compose run script` to start the script

TESTS
-----
To run tests locally, run `make test`
Tests use pytest and MongoMock, to perform tests without established db connection