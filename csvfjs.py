import csv, os, sys, json, pickle
import pandas as pd

def file_read(file):
    list = []
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
    except:
        pass
    try:
        with open(file) as json_file:
            reader = json.load(json_file)
    except:
        pass
    try:
        reader = pd.read_pickle(file)
    except:
        print(os.listdir(file))
        quit()
    for line in reader:
        list.append(line)
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


list = file_read(sys.argv[1])
print(list)
quit()
new_list = csv_define(list, sys.argv[3:])

csv_save(sys.argv[1], sys.argv[2], sys.argv[1], new_list)

quit()
