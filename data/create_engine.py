from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_DB
from urllib.parse import quote_plus
from contextlib import contextmanager


POSTGRES_USER_ENCODED = quote_plus(POSTGRES_USER)
POSTGRES_PASSWORD_ENCODED = quote_plus(POSTGRES_PASSWORD)

DATABASE_URI = f"postgresql://{POSTGRES_USER_ENCODED}:{POSTGRES_PASSWORD_ENCODED}@postgres:5432/{POSTGRES_DB}"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
