from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# Example SQLite database
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"

# For PostgreSQL use:
# DATABASE_URL = f'postgresql+asyncpg://postgres:***@db.db.xgatptoayglnefafjbrt.supabase.co:5432/postgres'

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base model
Base = declarative_base()


# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session