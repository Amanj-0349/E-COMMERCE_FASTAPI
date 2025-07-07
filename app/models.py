from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# User Table
class User(Base):
    __tablename__ = 'users'
    # here its shows that the table name is users in mysql
    # primary key - making column unique
    # index =True is for fast fast search
    # relationship shows that one users cann have multiple orders 
    # where as back_populates helps to establish the relationship between two mapped classes 
    # (and its bidirectional relationship) and if any changes occur on one class it will automatically occurs at the another end and better than the 'backref'


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # Relationship: A User can have many Orders
    orders = relationship('Order', back_populates='user')


# Product Table
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)

    # Relationship: A Product can appear in many Orders
    orders = relationship('Order', back_populates='product')


# Order Table
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    # Relationship: Each order is linked to one user and one product
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')
