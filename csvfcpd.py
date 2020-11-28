import csv
import sys
import pandas as pd
import os

with open('/Users/maciek/addresses.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        print(line)
    lines = list(reader)

def csv_write (file, directory, line, column, content):
    try:
        with open(file, "w") as f:
            writer = csv.writer(f)

    except:
        print(os.listdir(file))


# with open('/Users/maciek/csv/addresses.csv', "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Maciej", "Topolewski", "Katowice", "PL"])

f.close()

df = pd.read_csv('/Users/maciek/addresses.csv')
print(df)

print(lines)




#import petl - pandas pod csv

# f_open = sys.argv[1]
# f_read = sys.argv[2]
#for arg in sys.argv[3:]:
#      x


#
# '''
# loc = sys.argv[1]
# try:
#     df = pd.read_csv(loc)
#     print(df)
# except:
#     print(os.listdir(loc))
# '''


# num_rows = 0
# with open('/Users/maciek/addresses.csv', newline="") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(" ".join(line))
#         num_rows += 1
# print(num_rows)
