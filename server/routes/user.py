import typing
from fastapi import APIRouter, Request
import tortoise
from server.models.user import createUser, loginUser
from server.orm.models import User
from server.utils.error import PlatyHTTPException
import bcrypt
import os

router = APIRouter(tags=["user"])


@router.post("/")
async def register(data: createUser):
    try:
        salt: bytes = bcrypt.gensalt()
        peppa: bytes = (data.email + os.getenv("pepper")).encode("utf-8")
        hashpwd: bytes = bcrypt.hashpw(data.password.encode("utf-8") + peppa, salt)
        user = User(
            username=data.username,
            password=f"{hashpwd.decode('utf-8')}",
            email=data.email,
        )
        await user.save()
        return {"message": "User created successfully"}
    except Exception as e:
        if isinstance(e, tortoise.exceptions.IntegrityError):
            return PlatyHTTPException(
                409,
                typ=os.getenv("base_url") + "/problems/user/exists",
                title="User already exists",
                detail=f"User with email {data.email} already exists",
            )


@router.post("/login", tags=["auth"])
async def login(data: loginUser, req: Request):
    user = await User.filter(email=data.email).first()
    if user:
        if bcrypt.checkpw(
            data.password.encode("utf-8")
            + (user.email + os.getenv("pepper")).encode("utf-8"),
            user.password.encode("utf-8"),
        ):
            return {"message": "User logged in successfully"}
        else:
            return PlatyHTTPException(
                401,
                typ=os.getenv("base_url") + "/problems/authentication/invalid-password",
                title="Invalid password",
                detail="The password you entered is incorrect.",
            )
    else:
        return PlatyHTTPException(
            404, 
            typ=os.getenv("base_url")+ "/problems/authentication/user-not-found",
            title="User not found",
            detail="the user with email {} does not exist".format(data.email),
        )
