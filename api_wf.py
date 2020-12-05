import requests
import sys
import json
import csv


class WeatherForecast():

    def __init__(self):
        self.forecast_dict = {}
        self.forecast_date = None

    def main(self, api_key, forecast_date):
        querystring = {"lat":"50","lon":"19","unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"precipitation_probability",
        "apikey":api_key}
        response = requests.request("GET",
        "https://api.climacell.co/v3/weather/forecast/daily", params=querystring)
        self.forecast_date = forecast_date
        api_response_list = []
        for line in response.json():
            api_response_list.append(line)
        return_list = api_response_list[0]
        rain_list = return_list['precipitation_probability']
        rain = rain_list['value']
        if rain == 0:
            print("Nie będzie padać")
        elif rain <= 50:
            print("Nie wiem")
        else:
            print("Będzie padać")
        self.forecast_dict[forecast_date] = rain

    def csv_save(self, file_name):
        datafile = open(file_name)
        for line in datafile:
            if self.forecast_date in line:
                return
        with open(file_name, "a+", newline="") as file:
            writer = csv.writer(file, delimiter=',', lineterminator="\r")
            writer.writerow(self.forecast_dict.keys())
            writer.writerow(self.forecast_dict.values())
        file.close()

    def items(self, file):
        file = open(file, 'r')
        line = file.read().rstrip()
        print(line)

wf = WeatherForecast()
wf.main("{}".format(sys.argv[1]), "{}".format(sys.argv[2]))
wf.csv_save("dates.csv")
wf.items("dates.csv")
