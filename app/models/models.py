from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class SaleOrder(Base):
    __tablename__ = "sale_order"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state = Column(String)
    date_order = Column(DateTime)
    create_date = Column(DateTime)
    customer_id = Column(Integer)
    company_id = Column(Integer)
    currency_id = Column(Integer)
    amount_untaxed = Column(Numeric)
    amount_tax = Column(Numeric)
    amount_total = Column(Numeric)
    payment_term_id = Column(Integer)
    payment_mode = Column(String)
    item_total = Column(Numeric)

    lines = relationship("SaleOrderLine", back_populates="order")

class SaleOrderLine(Base):
    __tablename__ = "sale_order_line"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("sale_order.id"))
    name = Column(Text)
    price_unit = Column(Numeric)
    price_subtotal = Column(Numeric)
    price_total = Column(Numeric)
    discount = Column(Numeric)
    product_id = Column(Integer)
    product_uom_qty = Column(Numeric)
    qty_delivered = Column(Numeric)
    currency_id = Column(Integer)
    company_id = Column(Integer)
    create_date = Column(DateTime)

    order = relationship("SaleOrder", back_populates="lines")
