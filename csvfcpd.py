import csv
import sys
import pandas as pd
import os
list = []

with open('/Users/maciek/addresses.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader)
    for line in reader:
        list.append(line)
# for l in list:
#     print(l)

print(list[3][2])
quit()


def csv_read (file):
    try:
        list = []
        with open(file, "w") as f:
            reader = csv.reader(f)
            for line in reader:
                list.append(line)


#            csv_file = reader.writerow([content])
    except:
        print(os.listdir(file))
    return list

def csv_define (arg, list, row, column, content):
    for a in arg:
         x
    count_column = 0
    for count_row, line in enumerate(reader):
        count_column = len(line)
    items = count_row + count_column
    list[row]
    list[row][column] = content

#file_to_save = csv_file
def csv_save(directory, file_name, file_to_save):
    writer
    for l in list:
        writer.writerow(l)
    save = os.path.join(directory, file_name)
    file = open(save, 'w')
    file.write(file_to_save)
    file.close()

list = csv_read(sys.argv[1], sys.argv[3], sys.argv[4], sys.argv[5])

csv_define()

csv_save(sys.argv[2], 'addresses.csv', list)



# df = pd.read_csv('/Users/maciek/addresses.csv')
# print(df)


f_open = sys.argv[1]
f_read = sys.argv[2]
for arg in sys.argv[3:]:
     x




# with open('/Users/maciek/csv/addresses.csv', "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Maciej", "Topolewski", "Katowice", "PL"])



#
# f = open('mylist.csv', 'r')
# reader = csv.reader(f)
# mylist = list(reader)
# f.close()
# mylist[1][3] = 'X'
# my_new_list = open('mylist.csv', 'w', newline = '')
# csv_writer = csv.writer(my_new_list)
# csv_writer.writerows(mylist)
# my_new_list.close()


#import petl - pandas pod csv


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
