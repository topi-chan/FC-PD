import csv, os, sys, json, pickle
import pandas as pd


class FileReader:
    """Allows you to open and rewrite csv/json/pickle files"""

    def __init__(self, arg1, arg2, arg3):
        self.list = []
        self.new_list = []
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = []

    def file_read(self, file):
        try:
            with open(file, "r") as f:
                reader = csv.reader(f)
                for line in reader:
                    self.list.append(line)
                self.csv_define(self.list)
        except:
            pass
        try:
            with open(file) as json_file:
                reader = json.load(json_file)
                for line in reader:
                    self.list.append(line)
                self.json_define()
        except:
            pass
        try:
            reader = pd.read_pickle(file)
            for line in reader:
                self.list.append(line)
            self.pickle_define()
        except:
            # print(os.listdir(file))
            # quit()
            pass

    def csv_define(self, original_list):
        for arg in self.arg3:
            arg = arg.split(",")
            X = int(arg_number[0])
            Y = int(arg_number[1])
            content = arg_number[2]
            original_list[X][Y] = content
        self.new_list = original_list
        self.csv_save(self.arg2, self.arg1, self.new_list)

    def pickle_define(self, original_list, arg_number):
        for arg in arg_number:
            arg = arg.split(",")
            X = int(arg_number[0])
            Y = int(arg_number[1])
            content = arg_number[2]
            original_list[X][Y] = content
        new_list = original_list
        print(new_list)
        return new_list

    def csv_save(self, directory, file_name, file_to_save):
        with open(os.path.join(directory, file_name), "w") as f:
            writer = csv.writer(f)
            for line in file_to_save:
                writer.writerow(line)
            f.close()

# def json_save
#
# def pickle_save
fr = FileReader(sys.argv[1], sys.argv[2], sys.argv[3:])
fr.file_read(sys.argv[1])
quit()

print(fr.list)

new_list = csv_define(list, sys.argv[3:])
print(new_list)

csv_save(sys.argv[1], sys.argv[2], sys.argv[1], new_list)

quit()
