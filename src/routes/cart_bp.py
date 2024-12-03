from fastapi import APIRouter, Depends, Request
from controllers.cart_controller import (
    add_to_cart_item,
    read_cart,
    delete_cart_item
)

# Create a FastAPI APIRouter
cart_bp = APIRouter()

cart_bp.add_api_route("/add-to-cart-item/", add_to_cart_item, methods=["POST"])
cart_bp.add_api_route("/read-cart/{product_id}", read_cart, methods=["GET"])
cart_bp.add_api_route("/delete-cart-item/{cart_item_id}", delete_cart_item, methods=["DELETE"])