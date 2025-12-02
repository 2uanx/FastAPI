from sqlalchemy import Column, Integer, String, Float
from database import Base

class Order(Base): #bang don hang duoc tao trong db
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
