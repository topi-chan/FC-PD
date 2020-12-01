import requests

url = "https://api.climacell.co/v3/weather/forecast/daily"

querystring = {"lat":"50","lon":"19","unit_system":"si","start_time":"now",
"end_time":"2020-12-01T15:00:00","fields":"precipitation_probability",
"apikey":"PFtJhTkCKd9Xaua1zq70f8eeCjm6Bq0c"}

response = requests.request("GET", url, params=querystring)

print(response.text)
