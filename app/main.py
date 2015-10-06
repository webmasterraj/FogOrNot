import pandas as pd
import pws
import sfmap

# get list of active stations
# 9 api calls
stations = pws.SFStations()

#add correct neighborhood to each station
stations = sfmap.addNeighborhood(stations)

# create data frame with forecasts
# ~130 API calls
df = pd.concat(pws.forecastsDF(stations))

# add forecasts to JSON
sfmap.addForecastsToJSON(df)
sfmap.createNewJSON()

