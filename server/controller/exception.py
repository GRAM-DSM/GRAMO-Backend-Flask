from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError
from flask import abort

from server.model import session


def check_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
        except SQLAlchemyError or ProgrammingError as e:
            session.rollback()
            abort(418, 'database error')
        finally:
            session.close()
        return val
    return wrapper
