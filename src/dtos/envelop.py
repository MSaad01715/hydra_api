from typing import Any

from pydantic import BaseModel

class Envelop(BaseModel):

    TotalRecords: int = 0

    IsSuccessful: bool = True

    Status: str = ""

    Content: Any = None
    
