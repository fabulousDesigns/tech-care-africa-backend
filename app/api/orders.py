from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..models.order import Order as OrderModel
from ..schemas import order as order_schema

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.post("/create", response_model=order_schema.Order)
def create_order(order: order_schema.OrderCreate, db: Session = Depends(get_db)):
    db_order = OrderModel(**order.dict(), time=datetime.now())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=List[order_schema.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).offset(skip).limit(limit).all()
    return orders

@router.get("/{order_id}", response_model=order_schema.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.get("/customer/{customer_id}", response_model=List[order_schema.Order])
def read_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).filter(OrderModel.customer_id == customer_id).all()
    return orders