from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    user_name: str = Field(max_length=24)
    hashed_password: str = Field(max_length=24)
    is_blocked: bool
    email: str = Field(max_length=24)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)