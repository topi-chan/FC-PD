import csv, os, sys, json, pickle
import pandas as pd


class FileReader:
    '''Allows you to open a csv/json/pickle (or any other) files, then appends
    its content into a list with use of designed Class (name: 'File_formatReader')
    Pandas library is needed for PickleReader'''

    def __init__(self, filepath):
        self.filepath = filepath
        self.original_list = []
        self.new_list = []

#czy 'self' poniżej jest potrzebny?
    def detect(self, filepath):
        '''add another 'elif' if you want to add another file format'''
        path = os.path.splitext(filepath)
        extension = path[-1]
        if  extension == ".csv":
            return CsvReader(filepath)
        elif  extension == ".json":
            return JsonReader(filepath)
        elif extension == ".pickle":
            return PickleReader(filepath)
        else:
            print("Błąd - nie rozpoznano typu pliku")

    def file_read(self, file):
        filepath = ".".split(file)
        if filepath[-1] == "csv":
            with open(file, "r") as f:
                reader = csv.reader(f)
                for line in reader:
                    self.list.append(line)
                self.csv_define(self.list)
                self.csv_save('')
        elif filepath[-1] == "json":
            with open(file) as json_file:
                reader = json.load(json_file)
                for line in reader:
                    self.list.append(line)
            self.csv_define(self.list)
            self.csv_save('.csv')
        elif filepath[-1] == "pickle":
            reader = pd.read_pickle(file)
            for line in reader:
                self.list.append(line)
            self.csv_define(self.list)
            self.csv_save('.csv')

    def define(self, original_list):
        for arg in self.arg3:
            arg = arg.split(",")
            X = int(arg_number[0])
            Y = int(arg_number[1])
            content = arg_number[2]
            original_list[X][Y] = content
        self.new_list = original_list


class CsvReader(PathReader):
    '''Reads csv file and appends its content into a list within 'FileReader' Class'''

    def read(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.list.append(line)
            self.define(self.list)
#            self.csv_save('')

        zwracam obie klasy przez return CsvSave(filepath)

class JsonReader(PathReader):
    '''Reads json file and appends its content into a list within 'FileReader' Class'''

    def read(filepath):
        with open(filepath) as json_file:
            reader = json.load(json_file)
            for line in reader:
                self.list.append(line)
            self.define(self.list)

class PickleReader(PathReader):
    '''Reads pickle file and appends its content into a list within 'FileReader' Class'''

    def read(filepath):
        reader = pd.read_pickle(filepath)
        for line in reader:
            self.list.append(line)
        self.define(self.list)


class FileSave:
    '''It detects to which file format you want to save file as'''

    def __init__(self, filepath, file_readlist):
        self.file_list = file_list
        self.new_list = []
# z CsvReader list
        self.filepath = filepath

    def detect(filepath):
    if filepath[-1] == "csv":
        zwracam obie klasy przez return CsvSave(filepath)
    zwracam klase csv_save


    #
    # def csv_save(self, format):
    #     with open(os.path.join(self.arg2, self.arg1+format), "w") as f:
    #         writer = csv.writer(f)
    #         for line in self.new_list:
    #             writer.writerow(line)
    #     print(self.new_list)
    #
    #     sprawdzac czy istnieje plik

class CsvSave(FileSave):
    '''Rewrites and saves a CSV file returned from 'FileReader' Class'''


    def save(self):
        with open(os.path.join(self.arg2, self.arg1+format), "w") as f:
            writer = csv.writer(f)
            for line in self.new_list:
                writer.writerow(line)
#                self.csv_save()
        print(self.new_list)

class PickleSave:
    '''Saves a pickle file returned from 'FileReader' Class and then rewrited
    with 'csv_save' method within 'CsvSave' Class'''

#    @csv_define

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self.new_list, f)


class JsonSave:
    '''Rewrites and saves a json file returned from 'FileReader' Class'''
    json.dump
#    @csv_define


if os.path.isfile(sys.argv[1]):
    fr = FileReader(sys.argv[1], sys.argv[2], sys.argv[3:])
else:
    print("Błąd", "\n", os.listdir())
    quit()
fr.file_read(sys.argv[1])
quit()
reader = PathReader(filepath)
save = FileSave.detect(filepath2,reader.list)
save.save()
