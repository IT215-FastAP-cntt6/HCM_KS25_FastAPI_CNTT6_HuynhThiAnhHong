from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):

    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):

    password: str


class UserUpdate(BaseModel):

    email: EmailStr | None = None
    full_name: str | None = None
    is_active: bool | None = None


class UserResponse(UserBase):

    id: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )