import click
import csv
from pymongo import MongoClient

@click.command()
@click.argument('collection')
def read(collection):
    """Takes a csv file, converts each row into json, and inserts the rows into mongo """

    client = MongoClient('mongodb://localhost:27017/')
    db = client.get_database('test')

    cursor = db[collection].find()

    for row in cursor:
        # Do stuff here
        print(row['heading1'])

if __name__ == '__main__':
    read()