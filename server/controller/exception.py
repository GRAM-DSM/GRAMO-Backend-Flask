from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from flask import abort

from server.model import session


def check_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
        except:
            session.rollback()
            abort(418, 'database error')
        finally:
            session.close()
        return val
    return wrapper
