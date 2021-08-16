import csv
import sys

def pickup_dropoff_yielder(filename):
    with open(filename) as csv_file:
        dr = csv.reader(csv_file)
        is_first_line = True
        payment_type_index = 0
        pu_index, do_index = 0, 0
        for row in dr:
            if is_first_line:
                payment_type_index = row.index('payment_type')
                pu_index = row.index('PULocationID')
                do_index = row.index('DOLocationID')
                is_first_line = False
            elif len(row) > 0 and row[payment_type_index] == '3':
                yield row[pu_index], row[do_index]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Expecting a filename! Received {len(sys.argv) - 1} command line arguments.")
        sys.exit(0)

    filename = sys.argv[1]
    pu_zone_cnt, do_zone_cnt = 0,0
    for pu, do in pickup_dropoff_yielder(filename):
        if pu == '170':
            pu_zone_cnt += 1
        elif do == '170':
            do_zone_cnt += 1
    print(pu_zone_cnt)
    print(do_zone_cnt)


