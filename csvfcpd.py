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
print(lines)


def csv_write (file, line, column, content):
    column_counter = 0
    try:
        with open(file, "w") as f:
            writer = csv.writer(f)
            while True:
                x =
                y = next(reader)
            csv_file = writer.writerow(["Maciej", "Topolewski", "Katowice", "PL"])
    except:
        print(os.listdir(file))
    return csv_file

def csv_save(directory, file_name, file_to_save):
    save = os.path.join(directory, file_name)
    file = open(save, 'w')
    file.write(file_to_save)
    file.close()

csv_write(sys.argv[1], sys.argv[3], sys.argv[4], sys.argv[5])

csv_save(sys.argv[2], 'addresses.csv', csv_file)

# with open('/Users/maciek/csv/addresses.csv', "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Maciej", "Topolewski", "Katowice", "PL"])


df = pd.read_csv('/Users/maciek/addresses.csv')
print(df)





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
