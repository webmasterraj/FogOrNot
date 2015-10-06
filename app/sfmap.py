import json
from shapely.geometry import shape, Point
import pandas as pd
import numpy as np

SF = json.loads(open('static/geojson/sf.json', 'r').read())

def addNeighborhood(stations):
	for s in stations:
		s['neighborhood'] = whichNeighborhood(s)
	return stations


def whichNeighborhood(station):
	station_loc = Point(station['lon'], station['lat'])
	for neighborhood in SF['features']:
		poly = shape(neighborhood['geometry'])
		if poly.contains(station_loc):
			return neighborhood['properties']['neighborho']
	return None


def addForecastsToJSON(df):
	for neighborhood in SF['features']:
		neighborhood_name = neighborhood['properties']['neighborho']
		df_slice = df[df['neighborhood'] == neighborhood_name]
		forecasts_dict = df_slice.groupby('hour').aggregate(np.mean).to_dict()
		neighborhood['properties'].update(forecasts_dict['forecast'])

	
def createNewJSON():
	out_file = open("static/geojson/sf_forecasts.geojson", 'w')
	json.dump(SF, out_file, indent=1)
