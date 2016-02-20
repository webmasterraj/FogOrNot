from shapely.geometry import shape, Point
import pandas as pd
import numpy as np
import sql

SF = sql.getNeighborhoodsJSON()

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


def surroundingNeighborhoods(neighborhood):
    neighborhood_shape = shape(neighborhood['geometry'])
    surrounding_neighborhoods = []
    for other in SF['features']:
        if neighborhood_shape.touches(shape(other['geometry'])):
            surrounding_neighborhoods.append(other['properties']['neighborho'])
    return surrounding_neighborhoods


def addForecastsToJSON(df):
    empty_neighborhoods = []
    for neighborhood in SF['features']:
        neighborhood_name = neighborhood['properties']['neighborho']
        df_slice = df[df['neighborhood'] == neighborhood_name]
        print neighborhood_name, df_slice.shape
        if df_slice.shape[0] == 0:  # in case that neighborhood has no stations
            empty_neighborhoods.append(neighborhood)
#    print [n['properties']['neighborho'] for n in empty_neighborhoods]
        else:
            forecasts_dict = df_slice.groupby('hour').aggregate(np.mean).to_dict()
            neighborhood['properties'].update(forecasts_dict['forecast'])
    for neighborhood in empty_neighborhoods:
        neighborhood_name = neighborhood['properties']['neighborho']
        surrounding_neighborhoods = surroundingNeighborhoods(neighborhood)
        print "** NO STATIONS: {0}".format(neighborhood_name)
        print "** Using these instead: ", surrounding_neighborhoods
        print
        surrounding_forecasts_dfs = [df[df['neighborhood'] == other_name] for other_name in surrounding_neighborhoods]
        df_slice = pd.concat(surrounding_forecasts_dfs) if surrounding_forecasts_dfs \
            else df[df['neighborhood'] == neighborhood_name]
        forecasts_dict = df_slice.groupby('hour').aggregate(np.mean).to_dict()
        neighborhood['properties'].update(forecasts_dict['forecast'])
        print neighborhood_name, '\n', forecasts_dict, '\n\n'

	
def createNewJSON():
	sql.writeForecastsJSON(SF)
