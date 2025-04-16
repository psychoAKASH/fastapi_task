from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import SaleOrderCreate, SaleOrderOut
from app.db.database import SessionLocal
from app.crud import crud
from typing import List, Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sale-orders/", response_model=SaleOrderOut)
def create_order(order: SaleOrderCreate, db: Session = Depends(get_db)):
    return crud.create_sale_order_with_lines(db, order)

@router.get("/sale-orders/", response_model=List[SaleOrderOut])
def get_orders(customer_id: Optional[int] = None, company_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_sale_orders(db, customer_id, company_id)
