from fastapi import FastAPI
from pydantic import BaseModel
import redis

class Item(BaseModel):
    date:str
    distance:float
    light:float

app = FastAPI()
renderRedis = redis.Redis.from_url('rediss://red-clm0u4pfb9qs73966ia0:z8GgAGuZPDFfDdkxkrWjFyqfptcwu8gO@singapore-redis.render.com:6379')

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