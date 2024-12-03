from fastapi import APIRouter, Depends
from controllers.category_controller import (
    add_category,
    read_category,
    read_all_categories,
    #delete_category_service
)

# Create a FastAPI APIRouter
category_bp = APIRouter()

category_bp.add_api_route("/add-category/", add_category, methods=["POST"])
category_bp.add_api_route("/read-category/{category_id}", read_category, methods=["GET"])
category_bp.add_api_route("/read-all-categories/", read_all_categories, methods=["GET"])

