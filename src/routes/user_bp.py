from fastapi import APIRouter, Depends
from controllers.user_controller import (
    create_user,
    get_user,
    get_all_users
)

# Create a FastAPI APIRouter
user_bp = APIRouter()

user_bp.add_api_route("/create-user/", create_user, methods=["POST"])
user_bp.add_api_route("/get-user/{user_id}", get_user, methods=["GET"])
user_bp.add_api_route("/get-all-users/", get_all_users, methods=["GET"])
