from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
host = os.getenv("SQL_HOST")
port = os.getenv("SQL_PORT")
scheme = os.getenv("SQL_SCHEME")

URL_DATABASE = f"postgresql://{username}:{password}@{host}:{port}/{scheme}"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
