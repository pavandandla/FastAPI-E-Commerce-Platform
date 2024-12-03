from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # Store hashed passwords

    # One-to-many relationship with Order
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan", lazy="joined")

    def user_to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "orders": [order.order_to_dict() for order in self.orders]
        }


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # One-to-many relationship with Product
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan", lazy="joined")

    def category_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "products": [product.product_to_dict() for product in self.products]
        }


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)  # Inventory count
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    # Many-to-one relationship with Category
    category = relationship("Category", back_populates="products")

    def product_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category_id": self.category_id,
        }


class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Relationships
    user = relationship("User")
    product = relationship("Product")

    def cart_to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            
        }


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="Pending", nullable=False)

    # JSON field to store product details and quantities as [{"product_id": 1, "quantity": 2}, ...]
    items = Column(JSON, nullable=False)

    # Many-to-one relationship with User
    user = relationship("User", back_populates="orders")

    def order_to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_price": self.total_price,
            "status": self.status,
            "items": self.items,
        }

"""
orders =:
This attribute represents all the orders placed by a user. Each User object will have access to a list of its related
 Order objects via this attribute.

relationship("Order", ...):
Creates the relationship with the Order model.

back_populates="user":
Creates a bidirectional relationship. The Order model must define user = relationship("User", back_populates="orders") 
to establish this link.

cascade="all, delete-orphan",

lazy="joined":
Specifies eager loading, meaning related Order objects are loaded in the same query as the User objects for better 
performance.

category = relationship("Category", back_populates="products")
Defines the many-to-one relationship between the Product and Category models.

category =:
Represents the category to which a product belongs.

relationship("Category", back_populates="products"):
Links the Product model to the Category model, making this relationship bidirectional.

user = relationship("User")
Defines a many-to-one relationship with the User table.

user =:
Represents the user associated with an entity (e.g., Order or Cart).

relationship("User"):
Establishes the relationship with the User model, allowing access to the user object.
"""