import os
import json
from sqlalchemy import *
from sqlalchemy.sql import select

engine = create_engine(os.environ['DATABASE_URL'], echo=True)
metadata = MetaData()

SF_NEIGHBORHOODS_JSON_NAME = "sf_neighborhoods"

SF_FORECASTS_JSON_NAME = "sf_forecasts"

JSON_FILES = Table('json_files', metadata,
    Column(('id'), Integer, primary_key=True),
    Column(('name'), String),
    Column(('json'), Text),
    Column(('created_date'), Date)
)

conn = engine.connect()

def getNeighborhoodsJSON():
    s = select([JSON_FILES]).where(JSON_FILES.c.name == SF_NEIGHBORHOODS_JSON_NAME)
    result = conn.execute(s)
    row = result.fetchone()
    result.close
    return json.loads(row['json'])

def writeForecastsJSON(sf):
    ins = JSON_FILES.insert().values(
        name=SF_FORECASTS_JSON_NAME, 
        json=json.dumps(sf), 
        created_date="now"
    )
    conn.execute(ins)



# Do once to create sf neighborhoods JSON
# ins = json_files.insert().values(
#     name = SF_NEIGHBORHOODS_JSON_NAME,
#     json = f,
#     created_date = "now"
#     )
# result = conn.execute(ins)
