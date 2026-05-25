from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import AsyncSessionLocal

from core.database import get_db
from entities.xa import xa as geia_xa


class readonly_xa_repository:

    async def get_all_async(self):
        async with AsyncSessionLocal() as db:
            query = select(geia_xa)
            result = await db.execute(query)
            records = result.scalars().all()
            return records
    
    async def get_by_id_async(self, eiac: str):
         async with AsyncSessionLocal() as db:
            query = select(geia_xa).where(
                geia_xa.EndItemAcronymCode == eiac
            )
            result = await db.execute(query)
            record = result.scalars().first()
            return record
