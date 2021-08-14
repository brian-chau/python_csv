import csv
import sys

def func(filename):
    with open(filename) as csv_file:
        dr = csv.DictReader(csv_file)
        for row in dr:
            if row['payment_type'] in ['3']:
                yield row

if __name__ == '__main__':
    pu_zone_cnt, do_zone_cnt = 0,0
    for row in func('yellow_tripdata_2017-03.csv'):
        if row['PULocationID'] == '170':
            pu_zone_cnt += 1

        elif row['DOLocationID'] == '170':
            do_zone_cnt += 1
    print(pu_zone_cnt)
    print(do_zone_cnt)