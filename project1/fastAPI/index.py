from fastapi import FastAPI
from pydantic import BaseModel
import redis
from dotenv import load_dotenv


class Item(BaseModel):
    date:str
    distance:float
    light:float

import os

load_dotenv() #載入.env的環境變數
app = FastAPI()
renderRedis = redis.Redis.from_url(os.environ.get('redis'))

@app.post("/items/")
async def update_item(item:Item):
    print(item)
    return {'status':'ok'}

@app.get("/items/{date}/{distance}/{light}")
async def update_item1(date:str,distance:float,light:float):
    data = {
        'date' : date,
        'distance':distance,
        'light':light
    }
    renderRedis.lpush('pico_distance',distance)
    renderRedis.lpush('pico_light',light)
    print(data)
    return data