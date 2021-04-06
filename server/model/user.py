from sqlalchemy import Column, VARCHAR, Integer, Enum

from server.model import Base


class User(Base):
    __tablename__ = 'user_tbl'

    email = Column(VARCHAR(30), nullable=False, primary_key=True)
    password = Column(VARCHAR(100), nullable=False)
    email_status = Column(Integer, nullable=False)
    name = Column(VARCHAR(10), nullable=False)
    major = Column(Enum('ANDROID', 'IOS', 'BACKEND', 'DESIGN'))
