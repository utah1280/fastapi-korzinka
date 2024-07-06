from typing import List
from fastapi import Query
from fastapi import status
from typing import Optional
from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException
from core.models import db_helper
from crud import contact_crud as c
from core.schemas import contact_schemas
from sqlalchemy.ext.asyncio import AsyncSession

contacts_router = APIRouter(tags=["Contacts"])

@contacts_router.get("/get-contacts", response_model=List[contact_schemas.ContactResponse])
async def get_contacts(
    name: Optional[str] = Query(None, description="Filter by name."),
    email: Optional[str] = Query(None, description="Filter by email."),
    category: Optional[str] = Query(None, description="Filter by category."),
    order: Optional[str] = Query(None, description="Sort by created time."),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.get_all_contacts(name=name, email=email, category=category, order=order, session=session)
    return result

@contacts_router.get("/get-contacts/{id}", response_model=contact_schemas.ContactResponse)
async def get_contacts_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.get_contact_by_id(id, session=session)
        
    return result

@contacts_router.post("/new-contact", response_model=contact_schemas.ContactResponse)
async def add_new_contact(
    new_contact: contact_schemas.ContactCreateBody,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.add_new_contact(new_contact, session=session)
    
    return result

@contacts_router.patch("/update-contact/{id}", response_model=contact_schemas.ContactIdResponse)
async def update_contact(
    id: int,
    name: Optional[str] = Query(None),
    phone: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    address: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.update_contact(id, name=name, phone=phone, email=email, address=address, category=category, session=session)
    
    return result

@contacts_router.delete("/delete-contact/{id}", response_model=contact_schemas.ContactIdResponse)
async def delete_contact(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.delete_contact(id, session=session)
    
    return result