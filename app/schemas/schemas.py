from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SaleOrderLineCreate(BaseModel):
    name: str
    price_unit: float
    price_subtotal: float
    price_total: float
    discount: float
    product_id: int
    product_uom_qty: float
    qty_delivered: float
    currency_id: int
    company_id: int
    create_date: datetime

class SaleOrderCreate(BaseModel):
    name: str
    state: str
    date_order: datetime
    create_date: datetime
    customer_id: int
    company_id: int
    currency_id: int
    amount_untaxed: float
    amount_tax: float
    amount_total: float
    payment_term_id: int
    payment_mode: str
    item_total: float
    lines: List[SaleOrderLineCreate]

class SaleOrderOut(SaleOrderCreate):
    id: int
    class Config:
        orm_mode = True
