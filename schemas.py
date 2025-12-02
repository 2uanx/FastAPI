from pydantic import BaseModel
#class order cho ng quan li don hang
class OrderBase(BaseModel):
    customer_name: str #ten khach hang
    product_name: str #ten san pham
    quantity: int #so luong
    price: float #gia tien

#class order cua khach hang khi tao don hang moi
class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int #id don hang

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):# tao class de tra ve thong bao va don hang
    message: str
    order: Order
