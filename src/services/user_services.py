from sqlalchemy.orm import Session
from models.all_models import User

async def create_user_service(db: Session, form_data):
        existing_user = db.query(User).filter(User.username == form_data['username']).first()
        if existing_user:
            return {
                "status": "failed",
                "statusCode": 404, 
                "message": "User already exists",
            }
        new_user = User(
              username=form_data['username'],
              email=form_data['email'],
              password=form_data['password'])
        db.add(new_user)
        db.commit()
        return {
                "status": "success",
                "statusCode": 201,
                "message": "User created successfully",
                "data": new_user.user_to_dict()
            }

async def get_user_service(db: Session, user_id: int):
        user= db.query(User).filter(User.id == user_id).first()
        if not user:
            return {
                "status": "failed",
                "statusCode": 404,
                "message": "User not found"
            }
        return {
            "status": "success",
            "statusCode": 200,
            "message": "User found",
            "data": user.user_to_dict()
        }
         

async def get_all_users_service(db: Session):
        users = db.query(User).all()
        if not users:
            return {
                "status": "failed",
                "statusCode": 404,
                "message": "No users found"
            }
            
        return {
            "status": "success",
            "statusCode": 200,
            "data": [user.user_to_dict() for user in users]
        }
