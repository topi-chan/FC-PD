import requests
import sys

url = "https://api.climacell.co/v3/weather/forecast/daily"

def api_weather(api_key, forecast_date):
    querystring = {"lat":"50","lon":"19","unit_system":"si",
    "start_time":forecast_date,
    "end_time":"2020-12-01T15:00:00",
    "fields":"precipitation_probability",
    "apikey":api_key}
    return querystring

querystring = api_weather("{}".format(sys.argv[1]), "now")


response = requests.request("GET", url, params=querystring)


print(response.text)

#PFtJhTkCKd9Xaua1zq70f8eeCjm6Bq0c
#"now"
