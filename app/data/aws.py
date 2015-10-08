import os
import boto3
import json

def getJSON():
	s3 = boto3.resource('s3')
	SF_aws = s3.Object('fogornot', 'geojson/sf.json')
	SF_aws.download_file('sf.json')
	return json.loads(open('sf.json', 'r').read())


def writeJSON(forecasts):
	out_file = open("sf_forecasts.geojson", 'w')
	json.dump(forecasts, out_file, indent=1)
	out_file.close()	

	s3 = boto3.resource('s3')
	data = open("sf_forecasts.geojson", 'r').read()
	s3.Bucket('fogornot').put_object(Key='geojson/sf_forecasts.geojson', Body=data)