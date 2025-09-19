import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
# Get connection URL from environment or hardcode for testing
#DEV_DATABASE_URL = "postgresql+psycopg2://postgres1:yourpassword@172.29.41.66:5432/inventory"
load_dotenv() #this command finds for .env file and then 
DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

# Create engine
engine = create_engine(DEV_DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency-like function to get a DB session
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Simple test connection
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("✅ Connected to DB:", result.scalar())
    except Exception as e:
        print("❌✅❌✅ Connection failed:", e)
        
print("Loaded DB URL:", DEV_DATABASE_URL)  # for debugging
