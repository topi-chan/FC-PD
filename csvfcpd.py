import csv
import sys
import pandas as pd
import os

with open('/Users/maciek/csv/addresses.csv', newline="") as f:
    reader = csv.reader(f)
    lines = list(reader)

with open('/Users/maciek/csv/addresses.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Maciej", "Topolewski", "Katowice", "PL"])

f.close()

num_rows = 0
with open('/Users/maciek/addresses.csv', newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        print(" ".join(line))
        num_rows += 1
print(num_rows)

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
