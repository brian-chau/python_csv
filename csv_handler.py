import csv
import sys

def func(filename):
    with open(filename) as csv_file:
        dr = csv.reader(csv_file)
        is_first_line = True
        payment_type_index = 0
        pu_index, do_index = 0, 0
        pu_zone_cnt, do_zone_cnt = 0,0
        for row in dr:
            if is_first_line:
                payment_type_index = row.index('payment_type')
                pu_index = row.index('PULocationID')
                do_index = row.index('DOLocationID')
                is_first_line = False
            elif len(row) > 0 and row[payment_type_index] == '3':
                if row[pu_index] == '170':
                    pu_zone_cnt += 1

                elif row[do_index] == '170':
                    do_zone_cnt += 1
        print(pu_zone_cnt)
        print(do_zone_cnt)

if __name__ == '__main__':
    func('yellow_tripdata_2017-03.csv')
