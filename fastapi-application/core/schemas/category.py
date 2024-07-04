from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
    id: int
    label: str
    created_at: datetime