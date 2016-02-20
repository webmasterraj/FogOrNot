import urllib2
import json
import os


hourlyAPI = 'hourly10day/q/pws:'
geoAPI = 'geolookup/q/'
# currentCondidtionsAPI = 'conditions/q/pws:'

urlBase = 'http://api.wunderground.com/api'
key = os.environ['WU_KEY'] 

max_calls_per_minute = 10
max_calls_per_day = 400
# calls_today = 0
	# not tracking calls for now

MAX_FORECAST = 5


def urlBuilder(pws, api_type):
	return urlBase + '/' + key + '/' + api_type + pws + '.json'


def getLocations(coordinates):
	# takes tuple of coordinates and returns set of pws IDs near that coordinate
	loc = str(coordinates[0]) + "," + str(coordinates[1])
	url = urlBuilder(loc, geoAPI)
	raw_response = urllib2.urlopen(url).read()
	response = json.loads(raw_response)
	nearby_stations = response['location']['nearby_weather_stations']['pws']['station']
	# Was checking for latitude/longitude in san francisco, but it doesn't really matter right now
	# stations = {}
	# for station in nearby_stations:
	# 	if (min_latitude <= station['lat'] <= max_latitude) and (min_longitude <= station ['lon'] <= max_longitude):
	# 		stations['id'] = station
	return nearby_stations

# Don't need these functions, pulling lat/lon from nearby_stations graph
# Can deal with elevation later, if needed

# def getCurrentData(station):
# 	url = urlBuilder(str(station), currentCondidtionsAPI)
# 	raw_response = urllib2.urlopen(url).read()
# 	response = json.loads(raw_response)
# 	return response['current_observation']['display_location']

# def allStationData(stations):
# 	station_data = {}
# 	for station in stations:
# 		station_data['station'] = getCurrentData(station)
# 		sleep(60/(max_calls_per_minute - 1))
# 	return station_data


def getFogForecast(station_id):
	# given station_id, this returns a dictionary of timestamps to fog forecast, on scale of 0-4
	url = urlBuilder(station_id, hourlyAPI)
	raw_response = urllib2.urlopen(url).read()
	response = json.loads(raw_response)
	forecasts = []
	for hour in response['hourly_forecast']:
		tempDiff = int(hour['temp']['english']) - int(hour['dewpoint']['english']) 
		forecasts.append((int(hour['FCTTIME']['epoch']), max(MAX_FORECAST - tempDiff, 0)))
	return forecasts

