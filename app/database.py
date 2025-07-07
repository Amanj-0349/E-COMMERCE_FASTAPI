from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

# mysql connection url 
database_url = "mysql+pymysql://root:aman%20jha@localhost:3306/fastapi_ecommerce"


# sqlalchemy engine and session

engine = create_engine(database_url)
localsession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#base class for Orm models 
Base = declarative_base()


def get_db():
    db = localsession()  # Create new Session
    try:
        yield db         # Give this session to the route
    finally:
        db.close()