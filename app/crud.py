from sqlalchemy.orm import Session  
from app import models, schemas 
from fastapi import HTTPException

# db:Session ye database ke sth connection ke liye 
# user -> jo data api ke through ayega uske liye pydantic model se validate ho kr 
# .first() to return only first matching row from the table
# db.query() is just like select statement in sql
# skip and limit both are used for pagination 
#offset(skip) mtlb kitme records skip krne h 
# limit(limit) mtlb max kitne records fetch krne h 
# all() jitni bhi matching rows hh usko list ke form me dega 


# ********************************************************* #
# CRUD OPERATIONS FOR USERS
# ********************************************************* #

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,   
        email=user.email,
        hashed_password=user.hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
    return user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# ********************************************************* #
# CRUD OPERATIONS FOR PRODUCTS
# ********************************************************* #

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product


def update_product_price(db: Session, product_id: int, new_price: float):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        product.price = new_price
        db.commit()
        db.refresh(product)
    return product


def update_product_quantity(db: Session, product_id: int, new_quantity: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        product.quantity = new_quantity  
        db.commit()
        db.refresh(product)
    return product

# ********************************************************* #
# CRUD OPERATIONS FOR ORDERS
# ********************************************************* #

def create_order(db: Session, order: schemas.OrderCreate):
    product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')

    total_price = product.price * order.quantity  

    db_order = models.Order(
        user_id=order.user_id,        
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price   
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()  


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()


def delete_order(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return order


def update_order_quantity(db: Session, order_id: int, new_quantity: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
        if product:
            order.quantity = new_quantity
            order.total_price = product.price * new_quantity 
            db.commit()
            db.refresh(order)
    return order
