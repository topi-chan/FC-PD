import csv
import sys
import os

def csv_read(file):
    try:
        list = []
        with open(file, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                list.append(line)
    except:
        print(os.listdir(file))
        quit()
    return list

def csv_define(original_list):
    for arg in sys.argv[3:]:
        arg = arg.split(",")
        X = int(arg[0])
        Y = int(arg[1])
        content = arg[2]
        original_list[X][Y] = content
    new_list = original_list
    return new_list

def csv_save(original_file, directory, file_name, file_to_save):
    with open(original_file, "w") as f:
        writer = csv.writer(f)
    for line in file_to_save:
        csv_writer.writerow(line)
    save = os.path.join(directory, file_name)
    f.close()

list = csv_read(sys.argv[1])

new_list = csv_define(list)

csv_save(sys.argv[1], sys.argv[2], 'addresses.csv', new_list)

quit()
