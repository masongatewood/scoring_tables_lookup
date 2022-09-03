from fastapi import FastAPI
from scoring_tables import tables

app = FastAPI()


@app.get("/scoring_lookup")
async def lookup():
    pass