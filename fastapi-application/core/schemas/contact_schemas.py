from datetime import datetime
from pydantic import BaseModel
from .category_schemas import CategoryResponse



class ContactCreateBody(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    category: str

class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    category: CategoryResponse

    class Config:
        from_attributes = True

class ContactIdResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True