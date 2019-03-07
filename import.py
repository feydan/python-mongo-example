import click
import csv
from pymongo import MongoClient

@click.command()
@click.argument('filename')
@click.argument('collection')
def import_csv(filename, collection):
    """Takes a csv file, converts each row into json, and inserts the rows into mongo """

    client = MongoClient('mongodb://localhost:27017/')
    db = client.get_database('test')

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['newfield'] = 'newvalue'
            db[collection].insert_one(row)

if __name__ == '__main__':
    import_csv()