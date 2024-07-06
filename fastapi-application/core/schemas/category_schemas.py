from datetime import datetime
from pydantic import BaseModel



class CategoryResponse(BaseModel):
    id: int
    label: str
    created_at: datetime

    class Config:
        from_attributes = True

class CategoryIdResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True