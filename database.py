from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

print(f"db_url: {settings.database_url}")
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
