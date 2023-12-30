from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    date:str
    distance:float
    light:float

app = FastAPI()

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
    print(data)
    return data