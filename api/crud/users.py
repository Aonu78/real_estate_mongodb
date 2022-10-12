from fastapi.exceptions import HTTPException
# from ..db.mongo_db import AsyncIOMotorClient
from ..db.database import user_db
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from ..utils.auth_handler import JwtHandler
def userEntity(item)->dict:
    return {
        "first_name":item["first_name"],
        "email" : item["email"],
    }

def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]


async def register_user(user) -> JSONResponse:
    conn = user_db()
    auth_user = JwtHandler()
    hashed_password = auth_user.encode_password(user["password"])
    user["password"] = hashed_password
    new_user = conn["users"].insert_one(jsonable_encoder(user))

    try:

        created_user = conn["users"].find({"_id": new_user.inserted_id})
        # print(str(created_user))
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=usersEntity(created_user))

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'error':'We faced unexpected error.' , 'message': err})


async def update_user_data(email, new_data: dict = {}) -> JSONResponse:
    conn = user_db()
    update_result = await conn["users"].update_one({"email":email}, {"$set":new_data})

    if update_result.modified_count == 1:
        if updated_user := await conn["users"].find_one({"email":email}) is not None:

            return JSONResponse(status_code= status.HTTP_200_OK, content=updated_user)
    
    if (existing_user := await conn["users"].find_one({"email":email})) is not None:

        return JSONResponse(status_code = status.HTTP_200_OK, content=existing_user)


 
    raise HTTPException(status_code=500, detail=f"We can't find any user with this {email} email.")

async def get_single_user(name: str = "" , email: str = "") -> dict:
    conn = user_db()
    if name:
        db_student = await conn["users"].find({'name':name})
        
        if db_student:
            return db_student

    if email:
        db_user = conn["users"].find_one({'email':email})
        if db_user:
            return db_user