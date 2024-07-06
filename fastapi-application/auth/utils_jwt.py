import jwt
import bcrypt
from core.config import settings
from datetime import datetime, timedelta

def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_min,
):
    to_encode = payload.copy()
    now = datetime.now()
    expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded

async def decode_jwt(
    token: str,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    decoded = await jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded

async def hash_password(password: str):
    salt = await bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return await bcrypt.hashpw(pwd_bytes, salt)

async def validate_password(password: str, hashed_bytes: str):
    return await bcrypt.checkpw(
        password.encode(),
        hashed_password=hashed_bytes.encode()
    )

