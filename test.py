import csv
import sys

def func(filename):
    with open(filename) as csv_file:
        dr = csv.DictReader(csv_file)
        for row in dr:
            if row['payment_type'] in ['3']:
                yield row

if __name__ == '__main__':
    pu_zones, do_zones = {}, {}
    for row in func('yellow_tripdata_2017-03.csv'):
        if row['PULocationID'] not in pu_zones.keys():
            pu_zones[row['PULocationID']] = 1
        else:
            pu_zones[row['PULocationID']] += 1

        if row['DOLocationID'] not in do_zones.keys():
            do_zones[row['DOLocationID']] = 1
        else:
            do_zones[row['DOLocationID']] += 1
    print(pu_zones['170'])
    print(do_zones['170'])