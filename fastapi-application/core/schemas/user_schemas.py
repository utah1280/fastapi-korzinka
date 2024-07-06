from datetime import datetime
from pydantic import BaseModel



class TokenInfo(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    email: str

class UserSignIn(User):
    password: str