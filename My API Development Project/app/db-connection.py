import os 


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#create_engine---> used to create a string for database connection using the url 

DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

engine = create_engine(DEV_DATABASE_URL)

# still need to create a session so we use sessionmake

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=True)  #for better rollback support; increases controlling affect (so disabled autocommit)

Base = declarative_base() #gives the mapping functionality for models 

#now create a function

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

