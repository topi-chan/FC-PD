import csv, os, sys, json, pickle
import pandas as pd


class FileReader:
    """Allows you to open csv/json/pickle files, appends its content into list"""

    def __init__(self, arg1, arg2, arg3):
        self.list = []
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def file_read(self, file):
        filepath = ".".split(file)
        if filepath[1] == "csv":
            with open(file, "r") as f:
                reader = csv.reader(f)
                for line in reader:
                    self.list.append(line)
                self.csv_define(self.list)
                self.csv_save('')
        elif filepath[1] == "json":
            with open(file) as json_file:
                reader = json.load(json_file)
                for line in reader:
                    self.list.append(line)
            self.csv_define(self.list)
            self.csv_save('.csv')
        elif filepath[1] == "json":
            reader = pd.read_pickle(file)
            for line in reader:
                self.list.append(line)
            self.csv_define(self.list)
            self.csv_save('.csv')

class CsvSave:
    """Rewrites and saves a CSV file returned from 'FileReader' Class"""

    def __init__(self):
        self.list = []
        self.new_list = []

    def csv_define(self, original_list):
        for arg in self.arg3:
            arg = arg.split(",")
            X = int(arg_number[0])
            Y = int(arg_number[1])
            content = arg_number[2]
            original_list[X][Y] = content
        self.new_list = original_list

    def csv_save(self, format):
        with open(os.path.join(self.arg2, self.arg1+format), "w") as f:
            writer = csv.writer(f)
            for line in self.new_list:
                writer.writerow(line)
        print(self.new_list)

class PickleSave:
    """Saves a pickle file returned from 'FileReader' Class and then rewrited
    with 'csv_save' method within 'CsvSave' Class"""

#    @csv_define

    def pickle_save(self, format):
        with open(os.path.join(self.arg2, self.arg1+format), "w") as f:
            writer = csv.writer(f)
            for line in self.new_list:
                writer.writerow(line)
        print(self.new_list)


class JsonSave:
    """Rewrites and saves a json file returned from 'FileReader' Class"""

if os.path.isfile(sys.argv[1]):
    fr = FileReader(sys.argv[1], sys.argv[2], sys.argv[3:])
else:
    print("Błąd", "\n", os.listdir())
    quit()
fr.file_read(sys.argv[1])
quit()
