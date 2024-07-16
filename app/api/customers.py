from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..models import customer as customer_model
from ..schemas import customer as customer_schema

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.post("/create", response_model=customer_schema.Customer)
def create_customer(customer: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = customer_model.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/", response_model=list[customer_schema.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(customer_model.Customer).offset(skip).limit(limit).all()
    return customers

@router.get("/{customer_id}", response_model=customer_schema.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer