from fastapi import APIRouter, Body, Depends,HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ..models import user_model
from ..db.database import user_db
from ..utils.auth_handler import JwtHandler
from ..utils.auth_bearer import JwtBearer,get_current_user
from ..utils.duplicate_users import check_free_name_and_email
from ..crud.users import register_user,update_user_data
from ..crud.users import get_single_user
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
router = APIRouter()

@router.post("/user/signup", tags=["Users"])
async def create_user(user: user_model.UserSchema = Body(...)):
    db = user_db()
    user_dict = jsonable_encoder(user)
    await check_free_name_and_email(email=user_dict['email'])

    save_user =await register_user(user_dict)
    # return {"save_user":str(save_user)}
    return JSONResponse(content={"full_name":user.first_name+" "+user.last_name,"Email":user.email})


@router.post("/user/login", tags=["Users"])
async def user_login(user: user_model.UserLoginSchema = Body(...)):
    db = user_db()
    user_dict = jsonable_encoder(user)
    login_user = JwtHandler()
    # get_user = db.find_one({'name':name})
    get_user = await get_single_user(email=user_dict["email"])
    
    if get_user:
    
        if login_user.verify_password(user_dict["password"],get_user["password"]):
            return JSONResponse(status_code = status.HTTP_200_OK, content = jsonable_encoder(login_user.sign_jwt(user_dict["email"])))
    
    return { "error": "Wrong email / password" }

@router.get("/user",   tags=["Users"])
async def current_user(user_mail: str = Depends( JwtBearer() ) ):
    # print("**************************")
    # print(user_mail)
    get_user = await get_single_user(email=user_mail)
    print(get_user["email"])
    student: user_model.Student = user_model.Student(**get_user)
    if get_user:

        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(student))

# @router.put("/user/update", dependencies=[Depends(JwtBearer())], response_model=user_model.UserSchema,tags=["Users"])
# async def update_user(current_user: str = Depends( JwtBearer() ), new_data: user_model.UserUpdateSchema = Body(...)):

#     get_user_doc = await get_single_user(email=current_user)
    
#     user_fields = {k: v for k, v in new_data.dict().items() if v is not None}

#     if len(user_fields) >= 1:
#         result = await update_user_data(get_user_doc['email'],user_fields)
#         return result

#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Please enter 1 or more field to update.")