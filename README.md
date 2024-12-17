# **FastAPI E-Commerce Platform**

## **Description**

This project implements an **E-Commerce API** built with **FastAPI** and **SQLite**. Users can browse products, add items to their cart, and proceed to checkout. The API features product categories, inventory management, and order processing. It is designed with efficiency, scalability, and security in mind, making it ideal for managing an online store.



## **Features**

- **Secure Authentication and Authorization**  
    Provides a secure login and registration system, ensuring that users can safely access their shopping data.
    
- **Efficient Database Operations**  
    Uses **SQLite** with **FastAPI** and **SQLAlchemy** for optimized data storage and retrieval.
    
- **Inventory Management**  
    Manages the availability of products, tracking quantities, and updating stock during purchases.
    
- **Email Functionality**  
    Sends order confirmations and notifications via email after a successful transaction.
    
- **Environment Configuration**  
    Easy-to-manage environment configurations for both development and production.
    
- **Modular Code Organization**  
    Follows a modular architecture to ensure clean and maintainable code.
    
- **Standardized API Responses**  
    Consistent and clear JSON responses for API consumers.
    
- **Comprehensive Error Handling**  
    Proper error handling to gracefully communicate issues with users and maintain smooth functionality.
    


## Prerequisites

- Python 3.9+
- pip
- Virtual environment support
## **Libraries Used**

- **FastAPI** 
- **SQLAlchemy** 
- **SQLite** 
- **FastAPI-Mail** 
- **JWT** 
- **Python-dotenv** 



## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/pavandandla/FastAPI-E-Commerce-Platform.git
cd FastAPI-E-Commerce-Platform
```



### **2. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```



### **3. Install Dependencies**

```bash
pip install -r src/requirements.txt
```



### **4. Configure Environment Variables**

Create a `.env` file in the root directory with the following configuration:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///ecommerce.db
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
FLASK_ENV=development
```

- **SECRET_KEY**: A key for securely signing JWT tokens.
- **DATABASE_URL**: SQLite connection string.
- **EMAIL_HOST**: SMTP server for email functionality.
- **EMAIL_PORT**: Port for SMTP server.
- **EMAIL_USER**: Your email address for sending notifications.
- **EMAIL_PASSWORD**: Your email password.
- **FLASK_ENV**: Set to `development` for debugging.



### **5. Set Up the Database**

Run the following command to initialize the database and create necessary tables:

```bash
python src/init_db.py
```



### **6. Run the Application**

To run the FastAPI application, execute:

```bash
uvicorn src.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`





## **Example Workflow**

1. **Product Browsing**  
    Users can view the list of available products and product details via the `/products` endpoint.
    
2. **Adding Items to Cart**  
    Users can add products to their shopping cart via the `/cart` endpoint. The cart is stored temporarily until checkout.
    
3. **Checkout**  
    Once the cart is ready, users can complete their order via the `/checkout` endpoint. The order is processed, and inventory is updated.
    
4. **Email Notifications**  
    After completing an order, users will receive an order confirmation via email.
    


## **Environment Configuration**

Example `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///ecommerce.db
```



## **Contact**

For questions, suggestions, or issues, contact:

- GitHub: [pavandandla](https://github.com/pavandandla)
