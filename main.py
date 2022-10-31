import requests
import json
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    given = input("Enter National Park Code here: ")
    url = "https://developer.nps.gov/api/v1/alerts/"
    key = 'ZJvoWwN2zapHRpAyW8GdbtzylT3WOdt8eR9FXMKB'
    dynamic = "https://developer.nps.gov/api/v1/alerts?parkCode=" + given + "&api_key=ZJvoWwN2zapHRpAyW8GdbtzylT3WOdt8eR9FXMKB"
    response_api = requests.get(dynamic)

    data = response_api.text
    access = json.loads(data)
    return access
