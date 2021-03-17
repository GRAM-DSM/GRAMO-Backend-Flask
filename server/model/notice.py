from sqlalchemy import Column, VARCHAR, INTEGER, DATETIME, text

from server.model import Base


class Notice(Base):
    __tablename__ = 'notice_tbl'

    id = Column(INTEGER, nullable=False, primary_key=True)
    title = Column(VARCHAR(50), nullable=False)
    content = Column(VARCHAR(1000), nullable=False)
    user_email = Column(VARCHAR(30), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
