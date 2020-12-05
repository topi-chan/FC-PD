import requests
import sys
import json

d = {}

class WeatherForecast(self, api_key):

    def __init__(self, api_key):
        #tutaj chyba querystring i d nie musi być - może global?
        self.api_key = api_key
        self.querystring = {}
        self.d = {}

    def date(self, api_key, forecast_date):
        querystring = {"lat":"50","lon":"19","unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"precipitation_probability",
        "apikey":api_key}
        return querystring

    def listing(self):
        api_response_list = []
        for line in response.json():
            api_response_list.append(line)
        return_list = api_response_list[0]
        rain_list = return_list['precipitation_probability']
        rain = rain_list['value']
        return rain, api_response_list

    def items(self):
        tups = d.items()
        print(tups)

    def csv_read(file):
        list = []
        with open(file, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                list.append(line)

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
            writer.writerow(line)
        save = os.path.join(directory, file_name)
        f.close()



class FileReader:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.lines = []
        self.done = False

    def __iter__(self):
        if self.done:
            return iter(self.lines)
        return self

    def __next__(self):
        line = self.fp.readline()
        if not line:
            self.done = True
            self.fp.close()
            raise StopIteration
        self.lines.append(line[:-1])
        return line[:-1]

for line in FileReader("dane.txt"):
    print(line)


url = "https://api.climacell.co/v3/weather/forecast/daily"

try:
    answer = "{}".format(sys.argv[2])
except:
    answer = "{}".format("2020-12-02")

querystring = api_weather("{}".format(sys.argv[1]), answer)

response = requests.request("GET", url, params=querystring)


if rain == 0:
    print("Nie będzie padać")
elif rain <= 50:
    print("Nie wiem")
else:
    print("Będzie padać")
