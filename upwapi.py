# It that CSV, you will have latitude, longitude, month, year.
# I want to get temperature ,humidity, wind accordingly
#sample: -118.7533451,34.16965166,12,2017
import requests, json, csv, pandas as pd

df = pd.read_csv('/Users/maciek/lon_lat.csv')
lon = df._get_value(1, 'lon')
lat = df._get_value(1, 'lat')
class WeatherForecast():
    '''Allows you to retrive temp, humidity, wind from API'''

    def __init__(self):
        self.forecast_dict = {}
        self.forecast_date = None
        self.forecast_file_dict = {}
        self.list = []

    def main(self, api_key, forecast_date, lat, lon):
        querystring = {"lat":lat,"lon":lon,
            "unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"temp",
        "apikey":api_key}
        response = requests.request("GET",
        "https://api.climacell.co/v3/weather/forecast/daily", params=querystring)
        self.forecast_date = forecast_date
        api_response_list = []
        for line in response.json():
            api_response_list.append(line)
        querystring = {"lat":lat,"lon":lon,
            "unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"humidity",
        "apikey":api_key}
        response = requests.request("GET",
        "https://api.climacell.co/v3/weather/forecast/daily", params=querystring)
        self.forecast_date = forecast_date
        for line in response.json():
            api_response_list.append(line)
        querystring = {"lat":lat,"lon":lon,
            "unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"wind_speed",
        "apikey":api_key}
        response = requests.request("GET",
        "https://api.climacell.co/v3/weather/forecast/daily", params=querystring)
        self.forecast_date = forecast_date
        for line in response.json():
            api_response_list.append(line)
        humidity = api_response_list[0]
        temperature = api_response_list[1]
        windSpeed = api_response_list[2]
        return api_response_list

wf = WeatherForecast()
api_response_list = wf.main("PFtJhTkCKd9Xaua1zq70f8eeCjm6Bq0c", "2021-01-31",
    lat, lon)
print(api_response_list)
