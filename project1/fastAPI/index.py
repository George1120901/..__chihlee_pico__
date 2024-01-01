from fastapi import FastAPI
from pydantic import BaseModel
import redis
from dotenv import load_dotenv


class Item(BaseModel):
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

@app.post("/items/{lastNum}")
async def get_items(lastNum:int):
    #redis取出資料  
    distances = renderRedis.lrange('pico_distance',lastNum * -1,-1)
    light = renderRedis.lrange('pico_light',lastNum * -1,-1)

    #將byte string 轉換為 str
    distances_list = [item.decode('utf-8') for item in distances]
    light_list = [item.decode('utf-8') for item in light]

    #建立list_time:list[Item]
    list_item:list[Item] = []  
    for i in range(len(distances_list)):
        d = distances_list[i]
        l = light_list[i]
        #建立Pydantic實體
        item = Item(distance=float(d), light=float(l))        
        list_item.append(item)
    
    return list_item


