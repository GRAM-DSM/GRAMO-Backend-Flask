from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from server.config import MYSQL_DB_URL, REDIS_DB_URL

engine = create_engine(MYSQL_DB_URL)

Base = declarative_base()

session = sessionmaker(bind=engine)
Session = session()
