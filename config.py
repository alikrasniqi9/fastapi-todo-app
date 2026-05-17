from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'postgresql://postgres:kikiriki123@localhost:5432/myfirstdb_telusko_youtube_guy'
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

