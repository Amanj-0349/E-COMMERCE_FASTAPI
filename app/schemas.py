# pydantic model 

from pydantic import BaseModel ,Field
from typing import Annotated , Optional ,List

# ******************************************** **** for post operations ***************************************************#

class UserCreate(BaseModel):  
    username: Annotated[str, Field(..., description='name of the user')]
    email: Annotated[str, Field(..., description='email of the user')]
    hashed_password: Annotated[str, Field(..., description='password of the user')]

class ProductCreate(BaseModel): 
    name: Annotated[str, Field(..., description='name of the product')]
    description: Annotated[str, Field(..., description='description of the project')]
    price: Annotated[float, Field(..., description='contains the price of the product')]
    quantity: Annotated[int, Field(..., description='quantity of the product')]

class OrderCreate(BaseModel): 
    user_id: Annotated[int, Field(..., description='id of the user')]
    product_id: Annotated[int, Field(..., description='id of the product')]
    quantity: Annotated[int, Field(..., description='quantity of the product')]

# NOTE :  id hata diya hai kyunki ye DB khud generate karega.
# total_price bhi hata diya order_create se — kyunki ye backend calculate karega (price * quantity), client nahi bhejega.
# Tumhare CRUD code ke mutabik — total_price calculate ho raha hai DB side pe:



#********************************************************* for get operations *******************************************#



# note: get me id lena h  Kyuki jab tum kisi user/product/order ko fetch karte ho to uska unique identity (id) milta hai — 
# isse client side pe react/angular app ya koi frontend us specific item ko samajh sakta hai.

# Why orm_mode = True?
# SQLAlchemy ke models (jo tumhare DB me hain) — normal dict nahi hote — FastAPI ko kehna padta hai ki
# "ye SQLAlchemy object hai, dict ki tarah treat karna" — 
# tabhi wo model ka data (like user.id, user.email) pydantic model me convert karega.

class User(BaseModel):
    id:int
    username:str
    email:str
    hashed_password:str

    class Config:
         from_attributes = True 


class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int

    class Config:
         from_attributes = True 

class Order(BaseModel):
    id:int
    user_id:int
    product_id:int
    quantity:int
    total_price:float

    class Config:
         from_attributes = True 

#******************************************************for put operations *******************************************************#

class Userupdate(BaseModel):
    username: Annotated[Optional[str],Field(default=None)]
    email: Annotated[Optional[str],Field(default=None)]
    hashed_password :Annotated[Optional[str],Field(default=None)]

class Productupdate(BaseModel):
    name :Annotated[Optional[str],Field(default=None)]
    description:Annotated[Optional[str],Field(default=None)]
    price:Annotated[Optional[float],Field(default=None)]
    quantity:Annotated[Optional[int],Field(default=None)]

class Orderupdate(BaseModel):
    quantity:Annotated[Optional[int],Field(default=None)]
    total_price:Annotated[Optional[float],Field(default=None)]

    
# ************************* For Authentication Flow ****************************************

class UserLogin(BaseModel):
    email: Annotated[str, Field(..., description='email of the user')]
    password: Annotated[str, Field(..., description='plain password of the user')]

class Token(BaseModel):
    access_token: str
    token_type: str






