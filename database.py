from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://hm:Passw0rd@localhost:5432/myreco_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    encoding='utf-8',
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
