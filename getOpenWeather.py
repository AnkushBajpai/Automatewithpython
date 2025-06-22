#! python3
# Provides the 5-day forecasts in 3-hour intervals, for the location entered in the command line arguments

import json, requests, sys

APPID = 'a3d100acff171c399ddeec47538c1118'

# Compute location from command line arguments
if len(sys.argv) < 1:
    print('Usage: py getOpenWeather.py city_name')
    sys.exit()
location = sys.argv[1]

#Populating lat and lon as the built in geocoder API is deprecated
url1 = 'http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=5&appid=%s' % (location,APPID)
response1 = requests.get(url1)
response1.raise_for_status()

locationData = json.loads(response1.text)
lat = locationData[0]['lat']
print(locationData[0]['lat'])
lon = locationData[0]['lon']
print(locationData[0]['lon'])

# Download the JSON data from openweathermap.org's API
url2 =f'http://api.openweathermap.org/data/2.5/forecast?lat={round(lat,2)}&lon={round(lon,2)}&appid={APPID}'
response = requests.get(url2)
response.raise_for_status()

# Load JSON data into Python variable.
weatherData = json.loads(response.text)

# Uncomment to see the raw JSON text:
print(response.text)

w = weatherData['list']
i=0
while i<len(w):
    print('Weather predictions for %s:' % (location))
    print('For Date-Time -- %s:'% (w[i]['dt_txt']))
    print(w[i]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    i=i+1
