import os
import json
from sqlalchemy import *
from sqlalchemy.sql import select
from sqlalchemy.dialects.postgresql import JSONB


if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgres:///fogornot'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData()

SF_NEIGHBORHOODS_JSON_NAME = "sf_neighborhoods"

SF_FORECASTS_JSON_NAME = "sf_forecasts"

JSON_FILES = Table('json_files', metadata,
    Column(('id'), Integer, primary_key=True),
    Column(('name'), String),
    Column(('json'), JSONB),
    Column(('created_date'), Date)
)

metadata.create_all(engine) 
conn = engine.connect()

def getNeighborhoodsJSON():
    s = select([JSON_FILES]).where(JSON_FILES.c.name == SF_NEIGHBORHOODS_JSON_NAME)
    result = conn.execute(s)
    row = result.fetchone()
    result.close()
    return row['json']

def writeForecastsJSON(sf):
    ins = JSON_FILES.insert().values(
        name= SF_FORECASTS_JSON_NAME,
        json=sf, 
        created_date="now"
    )
    conn.execute(ins)



# # Do once to create sf neighborhoods JSON & upload first forecast file
# f = open("app/data/sf.json", 'r').read()
# j = json.loads(f)
# ins = JSON_FILES.insert().values(
#     name = SF_NEIGHBORHOODS_JSON_NAME,
#     json = j,
#     created_date = "now"
#     )
# result = conn.execute(ins)


# f = open("app/data/sf_forecasts.geojson", 'r').read()
# j = json.loads(f)
# ins = JSON_FILES.insert().values(
#     name = SF_FORECASTS_JSON_NAME,
#     json = j,
#     created_date = "now"
#     )
# result = conn.execute(ins)
