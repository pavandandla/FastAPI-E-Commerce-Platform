from sqlalchemy.orm import Session
from models.all_models import Category

async def create_category_service(db: Session, form_data):
        existing_category = db.query(Category).filter(Category.name == form_data['name']).first()
        if existing_category:
            return {
                "status": "failed",
                "statusCode": 404, 
                "message": "Category already exists",
            }
        new_category = Category(name=form_data['name'])
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return {
                "status": "success",
                "statusCode": 201,
                "message": "category created successfully",
                "data": new_category.category_to_dict()
            }

async def get_category_service(db: Session, category_id: int):
        category= db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return {
                "status": "failed",
                "statusCode": 404,
                "message": "Category not found"
            }
        return {
            "status": "success",
            "statusCode": 200,
            "data": category.category_to_dict()
        }
         

async def get_all_categories_service(db: Session):
        categories = db.query(Category).all()
        if not categories:
            return {
                "status": "failed",
                "statusCode": 404,
                "message": "No categories found"
            }
            
        return {
            "status": "success",
            "statusCode": 200,
            "data": [category.category_to_dict() for category in categories]
        }


