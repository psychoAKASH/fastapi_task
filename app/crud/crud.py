from sqlalchemy.orm import Session
from app.models.models import SaleOrder, SaleOrderLine
from app.schemas.schemas import SaleOrderCreate


def create_sale_order_with_lines(db: Session, order_data: SaleOrderCreate):
    order = SaleOrder(
        name=order_data.name,
        state=order_data.state,
        date_order=order_data.date_order,
        create_date=order_data.create_date,
        customer_id=order_data.customer_id,
        company_id=order_data.company_id,
        currency_id=order_data.currency_id,
        amount_untaxed=order_data.amount_untaxed,
        amount_tax=order_data.amount_tax,
        amount_total=order_data.amount_total,
        payment_term_id=order_data.payment_term_id,
        payment_mode=order_data.payment_mode,
        item_total=order_data.item_total
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    for line_data in order_data.lines:
        line = SaleOrderLine(**line_data.dict(), order_id=order.id)
        db.add(line)

    db.commit()
    return order


def get_sale_orders(db: Session, customer_id: int = None, company_id: int = None):
    query = db.query(SaleOrder)
    if customer_id:
        query = query.filter(SaleOrder.customer_id == customer_id)
    if company_id:
        query = query.filter(SaleOrder.company_id == company_id)
    return query.all()
