from sqlalchemy import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

from config import settings

url = URL(
    drivername=settings.DATABASE.DRIVER,
    username=settings.DATABASE.get("USERNAME", None),
    password=settings.DATABASE.get("PASSWORD", None),
    host=settings.DATABASE.get("HOST", None),
    port=settings.DATABASE.get("PORT", None),
    database=settings.DATABASE.get("NAME", None),
    query=settings.DATABASE.get("QUERY", None)
)
# url = "postgresql+psycopg://postgres:254940Sr@localhost:5432/ai_editor_dev"

engine: Engine = create_engine(
    url=url,
    echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
