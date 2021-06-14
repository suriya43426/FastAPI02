# Test CURL

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Coffee(BaseModel):
    name: str
    description: Optional[str] = None
    print: float
    start: int

coffee_db = [
    {
        'name': 'Espresso',
        'description': 'เป็นกาแฟดำที่เข้มข้นที่สุด',
        'print': '68',
        'start': '5'
    },
    {
        'name': 'Americano',
        'description': 'เป็นกาแฟดำ เติมน้ำร้อน',
        'print': '55',
        'start': '4'
    }
]

@app.get('/')
async def root():
    return coffee_db

@app.get('/coffee/{id}')
async def coffee_by_id(id: int):
    coffee = coffee_db[id-1]
    return coffee

# การเพิ่มข้อมูลลงใน database ใช้แค่ coffee
@app.post('/coffee')
async def create_coffee(coffee: Coffee):
    coffee = coffee_db.append(coffee)
    return coffee_db[-1]

# การลบข้อมูลจาก database ใช้อิง id
@app.delete('/coffee/{id}')
async def delete_coffee(id: int):
    coffee_db.pop(id-1)
    coffee = coffee_db[id - 1]
    result = {'msg', f"{coffee['name']} was delete!"}
    return result

# การอัพเดตข้อมูลใน database
@app.put('/coffee/{id}')
async def update_coffee(id: int, coffee: Coffee):
    coffee_db[id-1].update(**coffee.dict())
    result = {'msg': f"Coffee id {id} Update successful!"}
    return result

