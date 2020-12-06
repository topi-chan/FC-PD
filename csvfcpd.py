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

def csv_define(original_list, arg_number):
    for arg in arg_number:
        arg = arg.split(",")
        X = int(arg_number[0])
        Y = int(arg_number[1])
        content = arg_number[2]
        original_list[X][Y] = content
    new_list = original_list
    print(new_list)
    return new_list

def csv_save(original_file, directory, file_name, file_to_save):
    with open(os.path.join(directory, file_name), "w") as f:
        writer = csv.writer(f)
        for line in file_to_save:
            writer.writerow(line)
        f.close()


list = csv_read(sys.argv[1])

new_list = csv_define(list, sys.argv[3:])

csv_save(sys.argv[1], sys.argv[2], 'addresses.csv', new_list)

quit()
