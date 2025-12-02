from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Order as OrderModel
from schemas import OrderCreate, Order, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

# CREATE
@router.post("", response_model=OrderResponse, status_code=201) #khai basao duong dan
def create_order(order: OrderCreate, db: Session = Depends(get_db)):# ham va ten ham khai bao don hang moi cua khach
    new_order = OrderModel(**order.dict())#tao don hang moi, voi id tu tao, cac thuoc tinh con lai lay tu order
    db.add(new_order)#them don hang moi vao db
    db.commit() #luu thay doi vao db
    db.refresh(new_order)#tai lai don hang moi tao
    return {"message": "Tạo đơn hàng thành công", "order": new_order}

# READ ALL
@router.get("", response_model=list[Order]) #khai bao duong dan lay tat ca don hang
def get_orders(db: Session = Depends(get_db)): # ham va ten ham lay don
    return db.query(OrderModel).all() # tra ve ds don hang

# READ BY ID
@router.get("/{order_id}", response_model=OrderResponse) #khai bao duong dan lay don hang theo ID cua server
def get_order(order_id: int, db: Session = Depends(get_db)):# ham va ten ham lay don hang theo ID
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()# lay don hang trong ds
    if not order: 
        raise HTTPException(404, "Không tìm thấy đơn hàng") # kh tim thay id trung voi don hang
    return {"message": "Đơn hàng của bạn đã được đặt thành công", "order": order} # tra ve don hang neu tim thay id don hang

# UPDATE
@router.put("/{order_id}", response_model=OrderResponse) #khai bao duong dan de cap nhat don hang cua server
def update_order(order_id: int, updated: OrderCreate, db: Session = Depends(get_db)): #ham va ten ham cap nhat don hang cua khach da dat
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()# lay don hang trong ds
    if not order:
        raise HTTPException(404, "Không tìm thấy đơn hàng") # kh tim thay don hang theo id

    for key, value in updated.dict().items(): #cap nhat don hang
        setattr(order, key, value) #gan gia tri moi

    db.commit() #luu thay doi vao db
    db.refresh(order) #tai lai don hang sau khi cap nhat
    return {"message": "Đơn hàng của bạn đã được cập nhật", "order": order}

# DELETE
@router.delete("/{order_id}") #khai bao duong dan de xoa don hang
def delete_order(order_id: int, db: Session = Depends(get_db)): #ham va ten ham de xoa don hang
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first() #voi don hang duoc update dung de lay dung don can xoa
    if not order:
        raise HTTPException(404, "Không tìm thấy đơn hàng") #neu id kh trung

    db.delete(order) # xoa don hang
    db.commit() #luu thay doi vao db
    return {"message": "Xóa đơn hàng thành công"}
