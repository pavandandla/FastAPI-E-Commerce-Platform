from fastapi import Depends, Request
from sqlalchemy.orm import Session
from config.database import get_db
from services.cart_services import add_to_cart_service, get_cart_items_service, delete_cart_item_service

async def add_to_cart_item(request: Request, db: Session = Depends(get_db)):
        form_data = await request.form()
        return await add_to_cart_service(db, form_data)

async def read_cart(product_id: int, db: Session = Depends(get_db)):
        return await get_cart_items_service(db, product_id)


async def delete_cart_item(request: Request, cart_item_id: int, db: Session = Depends(get_db)):
    form_data = await request.form()
    quantity = form_data['quantity']
    # Pass both cart_item_id and quantity to the service layer
    return await delete_cart_item_service(db, cart_item_id, quantity)
 
