from sqlalchemy import select
from sqlalchemy import delete
from core.models import Contacts
from core.models import Categories
from sqlalchemy.orm import joinedload
from core.schemas import contact_schemas
from sqlalchemy.ext.asyncio import AsyncSession

async def get_all_contacts(
    name: str | None,
    email: str | None,
    category: str | None,
    order: str | None,
    session: AsyncSession
):
    query = select(Contacts).options(joinedload(Contacts.category)).order_by(Contacts.id)

    # !TODO - Filtering
    # if name:
    #     query.where(Contacts.name.ilike(f"%{name}%"))
    # if email:
    #     query.where(Contacts.email.ilike(f"%{email}"))

    result = await session.execute(query)
    contacts = result.scalars().all()

    return [contact_schemas.ContactResponse.model_validate(contact) for contact in contacts]

async def get_contact_by_id(id: int, session: AsyncSession):
    query = select(Contacts).options(joinedload(Contacts.category)).where(Contacts.id == id)
    contact = await session.scalar(query)

    if contact is None:
        return "error: contact with given id is not found"
    
    return contact_schemas.ContactResponse.model_validate(contact)

async def add_new_contact(
    new_contact: contact_schemas.ContactCreateBody,
    session: AsyncSession
):
    query = select(Contacts).where(Contacts.email == new_contact.email)
    result = await session.scalar(query)

    if result is not None:
        return "error: contact with given email already exists"
    
    query = select(Categories.id).where(Categories.label == new_contact.category)
    category_id = await session.scalar(query)
    
    if category_id is None:
        return "error: category with given name not found"

    new = Contacts(
        name=new_contact.name,
        phone=new_contact.phone,
        email=new_contact.email,
        address=new_contact.address,
        category_id=category_id
    )
    session.add(new)
    await session.commit()
    
    query = select(Contacts).options(joinedload(Contacts.category)).where(Contacts.id == new.id)
    result = await session.execute(query)
    contact = result.scalar()

    return contact_schemas.ContactResponse.model_validate(contact)
    
async def update_contact(
    id: int,
    name: str | None,
    phone: str | None,
    email: str | None,
    address: str | None,
    category: str | None,
    session: AsyncSession
):
    if email:
        query = select(Contacts).where(Contacts.email == email, Contacts.id != id)
        result = await session.scalar(query)
        if result is not None:
            return "error: contact with given email already exists"

    query = select(Contacts).options(joinedload(Contacts.category)).where(Contacts.id == id)
    result = await session.execute(query)
    contact = result.scalar_one_or_none()

    if contact is None:
        return "error: contact with given id not found"

    if name:
        contact.name = name
    if phone:
        contact.phone = phone
    if email:
        contact.email = email
    if address:
        contact.address = address

    if category:
        query = select(Categories).where(Categories.label == category)
        category_result = await session.scalar(query)
        if category_result is None:
            return "error: category with given name not found"
        contact.category_id = category_result.id

    await session.commit()

    return {"id": id}

async def delete_contact(id: int, session: AsyncSession):
    query = delete(Contacts).where(Contacts.id == id)
    result = await session.execute(query)
    await session.commit()
    
    return {"id": id}