from typing import Optional

from pydantic import EmailStr
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

# from ..db.mongo_db import AsyncIOMotorClient
from ..db.database import user_db
from ..crud.users import get_single_user


async def check_free_name_and_email(name: Optional[str] = None, email: Optional[EmailStr] = None) -> None:
    conn = user_db()
    if name:
        user_by_name = await get_single_user(name=name)

        if user_by_name:
            raise HTTPException( status_code= HTTP_422_UNPROCESSABLE_ENTITY, 
            detail= "User with this name already exists.")

    if email:
        user_by_email = await get_single_user(email=email)
        if user_by_email:
            raise HTTPException( status_code= HTTP_422_UNPROCESSABLE_ENTITY, 
            detail= "User with this email already exists.")
