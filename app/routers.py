from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app import models, schemas, crud ,utils
from app.database import get_db  # Use correct db session function

router = APIRouter()

# ===================================
#              USER ENDPOINTS
# ===================================

@router.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user after checking if email already exists.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db, user=user)


@router.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by user_id.
    """
    db_user = crud.get_user_by_id(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a paginated list of users.
    """
    return crud.get_users(db, skip=skip, limit=limit)


# ===================================
#            PRODUCT ENDPOINTS
# ===================================

@router.post('/products', response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product.
    """
    return crud.create_product(db, product=product)


@router.get('/products/{product_id}', response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get product by its ID.
    """
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return db_product


@router.get('/products', response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all products with pagination.
    """
    return crud.get_products(db, skip=skip, limit=limit)


@router.put('/products/{product_id}/price', response_model=schemas.Product)
def update_product_price(product_id: int, new_price: float, db: Session = Depends(get_db)):
    """
    Update price of a product.
    """
    updated_product = crud.update_product_price(db, product_id, new_price)
    if updated_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return updated_product


@router.delete('/products/{product_id}')
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by ID.
    """
    deleted_product = crud.delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return {'message': 'Product deleted successfully'}


# ===================================
#              ORDER ENDPOINTS
# ===================================

@router.post('/orders', response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """
    Create a new order.
    """
    return crud.create_order(db, order=order)


@router.get('/orders/{order_id}', response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    """
    Get order by ID.
    """
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail='Order not found')
    return db_order


@router.get('/orders', response_model=list[schemas.Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get list of all orders with pagination.
    """
    return crud.get_orders(db, skip=skip, limit=limit)


@router.put("/orders/{order_id}/quantity", response_model=schemas.Order)
def update_order_quantity(order_id: int, new_quantity: int, db: Session = Depends(get_db)):
    """
    Update the quantity of an order.
    """
    updated_order = crud.update_order_quantity(db, order_id, new_quantity)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order


@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """
    Delete an order by ID.
    """
    deleted_order = crud.delete_order(db, order_id)
    if deleted_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}

# -------------- Signup Route --------------
@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    hashed_pw = utils.hash_password(user.hashed_password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# -------------- Login Route --------------
@router.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user or not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    token = utils.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
