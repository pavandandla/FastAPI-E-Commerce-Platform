from sqlalchemy.orm import Session
from models.all_models import Product

async def create_product_service(db: Session, form_data):
        new_product = Product(
            name=form_data['name'], 
            description=form_data['description'],
            price=form_data['price'],
            stock=form_data['stock'], 
            category_id=form_data['category_id']
            )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return {
                        "status": "success",
                        "statusCode": 201,
                        "message": "product created successfully",
                        "data": new_product.product_to_dict()
                    }

async def get_product_service(db: Session, product_id: int):
        product =  db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return {
                "status":"failed",
                "statusCode": 404,
                "message":"No products found"
            }
        return {
            "status": "success",
            "statusCode": 200,
            "data": product.product_to_dict() 
        }

async def get_all_products_service(db: Session):
        products = db.query(Product).all()
        if not products:
            return {
                "status": "failed",
                "statusCode": 404,
                "message": "No products found"
            }
        return {
            "status": "success",
            "statusCode": 200,
            "data": [product.product_to_dict() for product in products]
        }

async def product_update_service(db: Session, product_id: int, form_data):
      product = db.query(Product).filter_by(id = product_id).first()
      if not product:
            return {
                "status": "success",
                "statusCode": 200,
                "message": "No products found"
            }
      else:
            if 'description' in form_data:
                product.name = form_data.get('name')
            if 'description' in form_data:
                product.description = form_data.get('description')
            if 'price' in form_data:
                product.price =  form_data.get('price')
            if 'stock' in form_data:
                product.stock =  form_data.get('stock')

            # Commit changes to the database
            db.commit()

            return {'status': "success", "statusCode": 200, "message": "Product updated successfully"}, 200


async def product_delete_service(db: Session, product_id: int):
      product = db.query(Product).filter_by(id = product_id).first()
      if not product:
            return {
                "status": "success",
                "statusCode": 200,
                "message": "No products found"
            }
      else:
            db.delete(product)
            db.commit()
            return {
                "status": "success",
                "statusCode": 200,
                "message": "Product deleted successfully"
            }