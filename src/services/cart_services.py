from sqlalchemy.orm import Session
from models.all_models import Cart,Product

async def add_to_cart_service(db: Session, form_data):
        
        existing_cart_item = db.query(Cart).filter(
            Cart.product_id == form_data['product_id'],
            Cart.user_id == form_data['user_id']  # Assuming you're filtering by user_id
        ).first()
        
        if existing_cart_item:
            product=db.query(Product).filter_by(id = form_data['product_id']).first()
            stock_quantity = product.stock

            if product.stock < int(form_data['quantity']):
                  return {
                        "status": "success",
                        "statusCode": 200,
                        "message": f"Product stock availability is {stock_quantity}, please choose less than stock"
                 } 
            
            else:
                    # Update the existing cart item
                    existing_cart_item.quantity += int(form_data['quantity'])
                    product.stock -= int(form_data['quantity'])
                    db.commit()
                    return {
                        "status": "success",
                        "statusCode": 201,
                        "message": "cart_item updated successfully",
                        "data": existing_cart_item.cart_to_dict()
                        } 
             
        else:
            product=db.query(Product).filter_by(id = form_data['product_id']).first()
            stock_quantity=product.stock

            if product.stock < int(form_data['quantity']):
                  return {
                        "status": "success",
                        "statusCode": 200,
                        "message": f"Product stock availability is {stock_quantity}, please choose less than stock"
                 } 
            else:
                 
                # Create a new cart item
                new_cart_item = Cart(product_id=form_data['product_id'], user_id=form_data['user_id'], quantity=form_data['quantity'])
                product.stock -= int(form_data['quantity'])
                db.add(new_cart_item)
                db.commit()
        
                return {
                            "status": "success",
                            "statusCode": 201,
                            "message": "cart_item created successfully",
                            "data": new_cart_item.cart_to_dict()
                        }

async def get_cart_items_service(db: Session, product_id: int):
        cart_item=db.query(Cart).filter(Cart.product_id == product_id).all()
        if not  cart_item:
                return {
                    "status": "failed",
                    "statusCode": 404,
                    "message": " cart_item not found"
                }
        return {
                "status": "success",
                "statusCode": 200,
                "data": [cart_item.cart_to_dict() for cart_item in cart_item]
            }

async def delete_cart_item_service(db: Session, cart_item_id: int, quantity: int):

    # Retrieve the cart item by ID
    cart_item = db.query(Cart).filter(Cart.id == cart_item_id).first()
    
    # Check if the cart item exists
    if not cart_item:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "Cart item not found"
        }

    # Check if quantity in cart is less than or equal to requested quantity
    if cart_item.quantity <= int(quantity):
        db.delete(cart_item)
        db.commit()
        return {
            "status": "success",
            "statusCode": 200,
            "message": "Cart item deleted successfully"
        }
    
    # If there is more quantity in cart than requested, adjust the quantity
    cart_item.quantity -= int(quantity)
    db.commit()
    return {
        "status": "success",
        "statusCode": 200,
        "message": "Quantity adjusted successfully",
        "data": cart_item.cart_to_dict()
    }