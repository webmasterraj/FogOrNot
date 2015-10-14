# FogOrNot

## An interactive map that predicts the San Francisco fog, using data from 130+ amateur weather stations

Fog or Not makes hourly predictions about how much fog there will be in San Francisco, for each neighborhood.

The predictions are based on micro-local weather data from hundreds of personal weather stations across the city. These are basically [small monitoring units](https://www.netatmo.com/en-US/product/weather-station) that weather geeks like me put on roofs and outside windows. 

Fog or Not is built on the [Weather Underground](https://www.wunderground.com/weather/api)API, which aggregates data streams from over 100K+ personal weather stations around the world. (If you're into weather, it's a really neat data stream to explore.)

The prototype in R lives [here](https://github.com/webmasterraj/FogOrNot_prototype).

The production back-end is in Python using Pandas, NumPy and Shapely, with Flask architecture running on Heroku. I created the visualization of forecasts by applying GeoJSON layer on top of Google Maps with jQuery/HTML5.
