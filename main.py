from fastapi import FastAPI, HTTPException
from models import Product
from config import session, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def init_db():
    db = session()

    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) #qekjo ma standard tek koka
            #db.add(database_models.Product(id=product.id, name=product.name, description=product.description, price=product.price, quantity=product.quantity))
        db.commit()

init_db()

@app.get('/products')
def get_all_products():
   # db = session()
   # db.query()
    return products

@app.get('/products/{id}')
def get_product_by_id(id: int) -> Product:
    for product in products:
        if product.id == id:
            return product
        
    raise HTTPException(status_code=404, detail="Product not found")

@app.post('/products')
def add_product(product: Product):
    return products.append(product)

@app.put('/products/{id}')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {
                "message": "Product updated successfully",
                "product": product
            }
        
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete('/products/{id}')
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"
        
    raise HTTPException(status_code=404, detail="Product not found")