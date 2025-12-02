from fastapi import FastAPI
from database import Base, engine
from routers import orders

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(orders.router)

@app.get("/")
def home():
    return {"message": "FastAPI với PostgreSQL và Routers hoạt động!"}
