from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta

# password hashing set up 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Sets the bcrypt algorithm for hashing passwords. 
# When user signs up — their password is hashed using this.

# JWT Config
SECRET_KEY = "your_secret_key"  # Use a real secret in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#  Converts plain password (like '12345') into hashed (unreadable string).
def hash_password(password: str):
    return pwd_context.hash(password)

# Compares user's login input (plain) with DB-stored hashed password.
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt