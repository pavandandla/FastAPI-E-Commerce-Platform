from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
#from starlette.middleware.sessions import SessionMiddleware
from routes.product_bp import product_bp
from routes.user_bp import user_bp
from routes.cart_bp import cart_bp
from routes.order_bp import order_bp
from routes.category_bp import category_bp
from config.database import init_db
import os

# Create the FastAPI app
app = FastAPI()



# Initialize the database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Include user routes
app.include_router(user_bp)
app.include_router(product_bp)
app.include_router(cart_bp)
app.include_router(order_bp)
app.include_router(category_bp)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


