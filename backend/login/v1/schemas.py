from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
