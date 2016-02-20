import pandas as pd
import numpy as np
import wu
from time import sleep


def SFStations():
	min_latitude = 37.724
	max_latitude = 37.810
	min_longitude = -122.519
	max_longitude = -122.360
	num_steps = 3
	latitude_range = np.linspace(min_latitude, max_latitude, num_steps)
	longitude_range = np.linspace(min_longitude, max_longitude, num_steps)
	sf_grid = [(x, y) for x in latitude_range for y in longitude_range]
	stations = []
	for loc in sf_grid:
		nearby_stations = wu.getLocations(loc)
		stations = stations + nearby_stations
		sleep(60/(wu.max_calls_per_minute - 1))
	stations = {s['id']:s for s in stations}.values() # deduping list
	return stations


def forecastsDF(stations):
    station_dfs = []
    for i, s in enumerate(stations):
        location = (s['lon'], s['lat'])
        fog_forecasts = wu.getFogForecast(s['id'])
        if fog_forecasts:
            hrs, forecasts = zip(*fog_forecasts)
            station_dfs.append(pd.DataFrame({
                'station_id' : [s['id'] for _ in range(len(hrs))],
                'station_location' : [location for _ in range(len(hrs))],
                'neighborhood' : [s['neighborhood'] for _ in range(len(hrs))],
                'hour' : hrs,
                'forecast' : forecasts
                }))
        print i, s['id'] # debugging purposes only
        sleep(60/(wu.max_calls_per_minute - 1))
    return station_dfs
