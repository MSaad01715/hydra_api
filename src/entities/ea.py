from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from ..core.database import Base

class ea(Base):
    end_item_acronym_code: Column(String, primary_key=True, index=True)
    