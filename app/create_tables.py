from app.database import engine, Base
from app import models  # This will load models.py — indirectly using it.

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
