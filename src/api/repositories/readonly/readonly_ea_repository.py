from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db

class readonly_ea_reposotory:
    async def get_all_async(db: AsyncSession = Depends(get_db)):
        return {"message": "Database connected"}