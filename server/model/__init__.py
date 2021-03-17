from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis

from server.config import MYSQL_DB_URL, REDIS_DB_URL

engine = create_engine(MYSQL_DB_URL)

Base = declarative_base()

session = sessionmaker(bind=engine)
Session = session()

Redis = redis.StrictRedis(host=REDIS_DB_URL, port=6379, db=0)
