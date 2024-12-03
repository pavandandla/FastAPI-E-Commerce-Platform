from fastapi import Depends, Request
from sqlalchemy.orm import Session
from config.database import get_db
from services.order_services import create_order_service, get_order_service, get_all_orders_service,update_order_service

async def place_order(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_order_service(db, form_data)

async def read_order(order_id: int, db: Session = Depends(get_db)):
    return await get_order_service(db, order_id)

async def read_all_orders(db: Session = Depends(get_db)):
    return await get_all_orders_service(db)

async def update_order(request: Request, order_id: int, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await update_order_service(db, order_id,form_data)

