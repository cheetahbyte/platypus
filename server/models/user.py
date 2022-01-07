from pydantic import BaseModel
from pydantic.networks import EmailStr


class createUser(BaseModel):
    username: str
    password: str
    email: EmailStr

class loginUser(BaseModel):
    email: EmailStr
    password: str