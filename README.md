# FastAPI02
test FastAPI 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/hello_ohm')
async def hello_ohm():
    return {'msg': 'Hello ohm is Awesome'}


@app.get('/{item_cal}')
async def cal_item(item_cal: int):
    return {'msg': f"{item_cal*2/100}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
