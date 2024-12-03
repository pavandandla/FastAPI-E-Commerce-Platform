from fastapi import Depends, Request
from sqlalchemy.orm import Session
from models.all_models import Category
from config.database import get_db, Base
from services.category_services import create_category_service, get_category_service, get_all_categories_service

async def add_category(request: Request,db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_category_service(db, form_data)


async def read_category(category_id: int, db: Session = Depends(get_db)):
    return await get_category_service(db, category_id)

async def read_all_categories(db: Session = Depends(get_db)):
    return await get_all_categories_service(db)




