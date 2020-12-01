import requests
import sys
import json

url = "https://api.climacell.co/v3/weather/forecast/daily"

def api_weather(api_key, forecast_date):
    querystring = {"lat":"50","lon":"19","unit_system":"si",
    "start_time":forecast_date,
    "end_time":forecast_date,
    "fields":"precipitation_probability",
    "apikey":api_key}
    return querystring




querystring = api_weather("{}".format(sys.argv[1]), "{}".format(sys.argv[2]))


response = requests.request("GET", url, params=querystring)


print(response.json())
