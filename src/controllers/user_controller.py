from fastapi import Depends, Request
from sqlalchemy.orm import Session
from config.database import get_db
from services.user_services import create_user_service, get_user_service, get_all_users_service

async def create_user(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_user_service(db, form_data)

async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await get_user_service(db, user_id)

async def get_all_users(db: Session = Depends(get_db)):
    return await get_all_users_service(db)