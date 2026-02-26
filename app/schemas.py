from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # pentru SQLAlchemy (Pydantic v2)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"