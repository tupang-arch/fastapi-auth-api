from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite local (ok pentru început)
DATABASE_URL = "sqlite:///./auth.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necesar pt sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()