from fastapi import APIRouter, Depends
from controllers.product_controller import (
    add_product,
    read_product,
    read_all_products,
    update_product,
    delete_product
)

# Create a FastAPI APIRouter
product_bp = APIRouter()

product_bp.add_api_route("/add-product/", add_product, methods=["POST"])
product_bp.add_api_route("/read-product/{product_id}", read_product, methods=["GET"])
product_bp.add_api_route("/read-all-products/", read_all_products, methods=["GET"])
product_bp.add_api_route("/update-product/{product_id}", update_product, methods=["PATCH"])
product_bp.add_api_route("/delete-product/{product_id}", delete_product, methods=["DELETE"])