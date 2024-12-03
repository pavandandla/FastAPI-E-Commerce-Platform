from fastapi import Depends, Request
from sqlalchemy.orm import Session
from config.database import get_db
from services.product_services import create_product_service, get_product_service, get_all_products_service,product_update_service, product_delete_service

async def add_product(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_product_service(db, form_data)


async def read_product(product_id: int, db: Session = Depends(get_db)):
    return await get_product_service(db, product_id)

async def read_all_products(db: Session = Depends(get_db)):
    return await get_all_products_service(db)

async def update_product(request: Request, product_id: int, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await product_update_service(db, product_id, form_data)

async def delete_product(product_id: int, db: Session = Depends(get_db)):
    return await product_delete_service(db, product_id)