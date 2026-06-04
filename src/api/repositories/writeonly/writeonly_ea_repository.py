from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import AsyncSessionLocal

from core.database import get_db
from entities.xa import xa as geia_xa

class writeonly_ea_reposotory:
    async def create_or_update_async(self, entity):
        async with AsyncSessionLocal() as db:
            existing = await db.get(
                geia_xa,
                entity.EndItemAcronymCode
            )
            if existing:

                # Update existing entity
                for key, value in entity.__dict__.items():

                    if key != "_sa_instance_state":

                        setattr(existing, key, value)

                db.add(existing)

            else:
                # Create new entity
                db.add(entity)

            await db.commit()
            return entity
        
    async def remove_async(self, eiac: str):
        async with AsyncSessionLocal() as db:
            entity = await db.get(geia_xa, eiac)

            if entity is None:
                return False

            await db.delete(entity)

            await db.commit()

            return True