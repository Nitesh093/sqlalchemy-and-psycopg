from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:Nitesh123@localhost/dbname')
Session = sessionmaker(bind=engine)
# Create tables if they don't exist
# Base.metadata.create_all(engine)
# Attach session to the app
session=Session()
