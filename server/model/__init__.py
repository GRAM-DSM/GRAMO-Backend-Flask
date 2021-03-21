from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis

from server.config import MYSQL_DB_URL

engine = create_engine(MYSQL_DB_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

Redis = redis.StrictRedis(host='localhost', port=6379, db=0)
