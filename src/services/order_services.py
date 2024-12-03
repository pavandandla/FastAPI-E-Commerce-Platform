from sqlalchemy.orm import Session
from models.all_models import Order,Product
import json

async def create_order_service(db: Session, form_data):
    # Calculate total price based on product prices and quantities
    items = form_data['items']
    if isinstance(items, str):
        items = json.loads(items)  # Convert from string to JSON if necessary

    total_price = 0.0
    for item in items:
        product = db.query(Product).filter(Product.id == int(item['product_id'])).first()
        if product.stock < int(item['quantity']):
             return {
                        "status": "success",
                        "statusCode": 200,
                        "message": f"{product.name} has stock availability is {product.stock}, please choose less than stock"
                 } 
             
        else:
            total_price += product.price * item['quantity']
            
    if total_price > 0.0:
        # Create new order with calculated total price
        new_order = Order(
            total_price=total_price,  # Calculated dynamically
            status=form_data.get('status', 'Pending'),# Default to 'Pending' if no status provided
            user_id=form_data['user_id'],
            items=form_data['items']  # Assumes form_data['items'] is already in JSON format
        )

        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        return {
            "status": "success",
            "statusCode": 201,
            "message": "Order created successfully",
            "data": new_order.order_to_dict()
        }

async def get_order_service(db: Session, order_id: int):
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return {
                "status": "success",
                "statusCode": 200,
                "message": "Order not found"
                }
        return {
            "status": "success",
            "statusCode": 200,
            "data": order.order_to_dict()
        }

async def get_all_orders_service(db: Session):
        orders = db.query(Order).all()
        if not orders:
            return {
                "status": "success",
                "statusCode": 200,
                "message": "No orders found"
            }
        return {
            "status": "success",
            "statusCode": 200,
            "data": [order.order_to_dict() for order in orders]
        }

async def update_order_service(db: Session, order_id: int, form_data):
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return {
                "status": "success",
                "statusCode": 200,
                "message": "Order not found"
                }
        else:
             order.status=form_data['status']
             db.commit()
             return {
                    "status": "success",
                    "statusCode": 200,
                    "message": "Order updated successfully"
                }
            