from .db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CommonQueryParams:
    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        if self.offset < 0:
            self.offset = 0
        self.limit = limit

        if self.limit < 0:
            self.limit = 10
