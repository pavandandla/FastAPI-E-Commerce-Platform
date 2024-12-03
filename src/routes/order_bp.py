from fastapi import APIRouter, Depends
from controllers.order_controller import (
    place_order,
    read_order,
    read_all_orders,
    update_order
)

# Create a FastAPI APIRouter
order_bp = APIRouter()

order_bp.add_api_route("/place-order/",place_order, methods=["POST"])
order_bp.add_api_route("/read-order/{order_id}", read_order, methods=["GET"])
order_bp.add_api_route("/read-all-orders/", read_all_orders, methods=["GET"])
order_bp.add_api_route("/update-order/{order_id}", update_order, methods=["PATCH"])
