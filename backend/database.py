from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

DATABASE_URL = "postgresql://postgres:postgres@localhost/todolist"

engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # Default number of connections to maintain
    max_overflow=10,  # Allow up to 10 connections beyond pool_size
    pool_timeout=30,  # Timeout in seconds for getting a connection from pool
    pool_pre_ping=True,  # Enable connection health checks
    poolclass=QueuePool  # Explicitly specify QueuePool
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()