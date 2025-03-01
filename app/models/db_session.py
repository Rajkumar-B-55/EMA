from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from settings import settings

sql_uri = settings.DATABASE_URL

engine = create_engine(url=sql_uri, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)




async def get_db():
    async with SessionLocal() as session:
        yield session
