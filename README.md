# FogOrNot

A map that predicts the San Francisco fog, using data from 130 personal rooftop weather stations. [Live version here](http://fogornot.com).

##GaSiProMo

I'm using this project for [GaSiProMo](https://codelympics.io/projects/3). My goal for the month is to build a machine learning algorithm that does a better job forecasting fog than my current version. I'll be keeping a log of my progress through the month here.

If you have feedback, please share on my GaSiProMo Reddit [thread](https://www.reddit.com/r/codelympics/comments/3r0nvz/gasipromo_fog_or_not_project/)!

###*11/1/2015*
GaSiProMo begins! This week, I'm going to find a training data set – times when flights were delayed at SFO airport because of fog, and the preceding weather conditions. I'm going to use this to train a forecasting model for fog. Read the [full log entry](https://github.com/webmasterraj/GaSiProMo/blob/master/project_logs/log_10-17-2015.md) for more info.

***

## About

[Live version here](http://fogornot.com)

Fog or Not makes hourly predictions about how much fog there will be in San Francisco, for each neighborhood.

The predictions are based on micro-local weather data from hundreds of personal weather stations across the city. These are basically [small monitoring units](https://www.netatmo.com/en-US/product/weather-station) that weather geeks like me put on roofs and outside windows. 

Fog or Not is built on the [Weather Underground](https://www.wunderground.com/weather/api) API, which aggregates data streams from over 100K+ personal weather stations around the world. (If you're into weather, it's a really neat data stream to explore.)

The prototype in R lives [here](https://github.com/webmasterraj/FogOrNot_prototype).

The production back-end is in Python using Pandas, NumPy and Shapely, with Flask architecture running on Heroku. I created the visualization of forecasts by applying GeoJSON layer on top of Google Maps with jQuery/HTML5.
