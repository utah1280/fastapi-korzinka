from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException, status

import auth.utils_jwt as a

from core.models import Users
from core.models import db_helper
from core.schemas import user_schemas

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

auth_router = APIRouter(tags=["Auth"])

# !TODO: Вынести в отдельный пакет
async def validate_auth_login(
    user: user_schemas.UserLogin,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    query = select(Users).where(Users.username == user.username)
    result = await session.scalar(query)

    if result is None or not a.validate_password(user.password, result.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="error: invalid username or password")
    
    return result

@auth_router.post("/login", response_model=user_schemas.TokenInfo)
async def login(
    user: user_schemas.User = Depends(validate_auth_login)
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = a.encode_jwt(jwt_payload)
    return user_schemas.TokenInfo(
        access_token=token,
        token_type="Bearer"
    )