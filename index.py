from fastapi import FastAPI
from prediction import get_prediction
import json

app = FastAPI()

@app.get("/")
async def root():
    print("we are in root...")
    return { "message": "index route of api", "status": 200 }

@app.get("/prediction/{symbol}")
async def get_pred(symbol):
    print(symbol)
    data =  get_prediction(symbol)
    print("Data: ",data)
    data = json.dumps(data, default=str)
    # print("Data date: ", data.one_week_dates)
    # data = json.dumps(data)
    return data
    # return {"symbol": symbol}
