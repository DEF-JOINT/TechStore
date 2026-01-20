from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from enum import Enum
from datetime import datetime
import uuid

class UserRole(str, Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    MODERATOR = "moderator"

class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Имя пользователя должно содержать только буквы и цифры')
        return v

class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Пароль должен содержать минимум 8 символов')
        return v

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None

class UserInDB(UserBase):
    id: uuid.UUID
    is_active: bool
    is_verified: bool
    role: UserRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserResponse(UserInDB):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[uuid.UUID] = None
    role: Optional[UserRole] = None
