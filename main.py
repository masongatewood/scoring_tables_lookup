from fastapi import FastAPI
import scoring_tables
import constants
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/scoring_lookup")
async def lookup(event: constants.Events, time: str):
    results = scoring_tables.middle_distance.loc[
        (scoring_tables.middle_distance[event].str.contains(time))
    ]
    dict_df = results.to_dict(orient='records')
    return dict_df