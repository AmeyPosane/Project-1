from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from models import Plant
from dp import supabase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/plants")
def get_plants():
    return supabase.table("plants").select("*").execute().data

@app.post("/plants")
def add_plant(plant: Plant):
    supabase.table("plants").insert({
        "name": plant.name,
        "price": plant.price,
        "quantity": plant.quantity
    }).execute()
    return {"message": "Plant Added Successfully"}

@app.get("/low-stock")
def low_stock():
    return supabase.table("plants").select("*").lt("quantity", 6).execute().data

@app.delete("/plants/{plant_name}")
def delete_plant(plant_name: str):
    supabase.table("plants").delete().eq("name", plant_name).execute()
    return {"message": "Plant Deleted Successfully"}

@app.put("/plants/{plant_name}")
def update_price(plant_name: str, new_price: int):
    supabase.table("plants").update({
        "price": new_price
    }).eq("name", plant_name).execute()
    return {"message": "Price Updated Successfully"}

@app.put("/plants/quantity/{plant_name}")
def update_quantity(plant_name: str, new_quantity: int):
    supabase.table("plants").update({
        "quantity": new_quantity
    }).eq("name", plant_name).execute()
    return {"message": "Quantity Updated Successfully"}

@app.get("/search/{name}")
def search(name: str):
    return supabase.table("plants").select("*").eq("name", name).execute().data

@app.post("/orders")
def create_order(
    customer_name: str,
    plant_name: str,
    quantity: int,
    total_price: int
):
    supabase.table("orders").insert({
        "customer_name": customer_name,
        "plant_name": plant_name,
        "quantity": quantity,
        "total_price": total_price
    }).execute()
    return {"message": "Order Placed Successfully"}

@app.get("/orders")
def get_orders():
    return supabase.table("orders").select("*").execute().data
