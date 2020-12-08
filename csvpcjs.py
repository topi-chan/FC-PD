import csv, os, sys, json, pickle
import pandas as pd


class FileReader:
    '''Allows you to open a csv/json/pickle (or any other) files with use of
    designed Class (name: 'File_formatReader'), appends its content into a list,
    then changes its content, according to given atributes.
    For saving a file call the 'FileSave' Class.
    Pandas library is needed solely for PickleReader.'''

#'change_list' to będzie nasz argv[3:]
    def __init__(self, filepath, change_list):
        self.filepath = filepath
        self.change_list = change_list
        self.original_list = []
        self.new_list = []

#czy 'self' poniżej jest potrzebny? czy 'path' jest, skoro pobrany w __init__?
    def detect(self):
        '''add another 'elif' if you want to add another file format'''
        path = os.path.splitext(self.filepath)
        extension = path[-1]
        if  extension == ".csv":
            return CsvReader(self.filepath)
        elif  extension == ".json":
            return JsonReader(self.filepath)
        elif extension == ".pickle":
            return PickleReader(self.filepath)
        else:
            print("Błąd - nie rozpoznano typu pliku")

    def define(self):
        for arg in self.change_list:
            arg = arg.split(",")
            X = int(arg_number[0])
            Y = int(arg_number[1])
            content = arg_number[2]
            self.original_list[X][Y] = content
        self.new_list = self.original_list

class CsvReader(FileReader):
    '''Reads csv file and passes its content into a list within 'FileReader' Class'''

    def read(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.original_list.append(line)
            self.define(self.original_list)

class JsonReader(FileReader):
    '''Reads json file and passes its content into a list within 'FileReader' Class'''

    def read(filepath):
        with open(filepath) as json_file:
            reader = json.load(json_file)
            for line in reader:
                self.original_list.append(line)
            self.define(self.original_list)

class PickleReader(FileReader):
    '''Reads pickle file and passes its content into a list within 'FileReader' Class'''

    def read(filepath):
        reader = pd.read_pickle(filepath)
        for line in reader:
            self.original_list.append(line)
        self.define(self.original_list)


class FileSave():
    '''It detects to which file format you want to save file as, then passes
    a filepath argument into its derived class (namely: File_formatSave)'''

    def __init__(self, filepath, file_read_list):
        self.filepath = filepath
        self.file_read_list = file_read_list

    def detect(self, filepath):
        '''add another 'elif' if you want to add another file format'''
        path = os.path.splitext(filepath)
        extension = path[-1]
        if  extension == ".csv":
            return CsvSave(filepath)
        elif  extension == ".json":
            return JsonSave(filepath)
        elif extension == ".pickle":
            return PickleSave(filepath)
        else:
            print("Błąd - nie rozpoznano typu pliku")


class CsvSave(FileSave):
    '''Rewrites and saves a CSV file content, received from 'FileReader' Class'''

#czy trzeba przy wywołaniu tej funkcji w FileSave wywoływać także metodę 'save'?
    def save(filepath):
        pathname = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        with open(os.path.join(pathname, filename), "w") as f:
            writer = csv.writer(f)
            for line in self.file_read_list:
                writer.writerow(line)


class PickleSave(FileSave):
    '''Saves a pickle file content, received from 'FileReader' Class'''

    def save(filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self.file_read_list, f)


class JsonSave(FileSave):
    '''Rewrites and saves a json file received from 'FileReader' Class'''

    def save(filepath):
        with open(filepath, 'w') as f:
            json.dump(self.file_read_list, f)


if os.path.isfile(sys.argv[1]):
    fr = FileReader(sys.argv[1], sys.argv[3:])
else:
    print("Błąd", "\n", os.listdir())
    quit()
fr.detect()
save = FileSave(sys.argv[2],fr.new_list)
save.detect()
quit()
