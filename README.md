# python-mongo-example
Simple project showing python and mongo working together locally

## Requirements
1. Install Docker: https://hub.docker.com/search/?type=edition&offering=community
2. Setup python environment:
    1. You may want to use virtualenv to create a separate python environment
    2. `pip install -r requirements.txt`

I've tested this script in python 3.7.  I'm not sure if it works in other versions.

## Installation
`docker-compose up`

The mongo server runs inside of docker container to make installing the database easier and more isolated.  Keep this terminal running to keep the server running.  The server stops when you control-c out of it.

## Importing Csv Data
`python import.py test.csv test_collection`

This is a simple example of inserting data into a mongo collection from a csv file

## Reading data from mongo
`python read.py test_collection`

This reads from `test_collection` and prints out the `heading1` of each document

## Connecting to the mongo shell
`docker-compose exec mongo mongo`

This runs the `mongo` command on the `mongo` container.  From here you can connect to a database and query collections.  Examples below:
1. `use test` connects to the test database
2. `db.test_collection.find().pretty()` gets the first 10 documents in the test collection
3. `db.test_collection.find({heading2:'row2c2'}).pretty()` gets documents where 'heading2' = 'row2c2'