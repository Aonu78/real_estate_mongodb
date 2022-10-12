from operator import ge
from ..crud.users import get_single_user
from ..crud.property import get_single_property,get_complete_property
from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from ..utils.auth_bearer import JwtBearer
from bson import ObjectId
from ..models.property_post import Home_fect
# from app.varification import Authentication
from ..models.property_get import propertiesEntity
from ..models import property_get
from ..db.database import property_db
from fastapi import status,HTTPException
from bson import ObjectId
from fastapi import File, UploadFile
from typing import List
import os

router = APIRouter(
    tags=['Insertion'],
    prefix="/property"
)
ROOT_PATH = "upload/"

@router.post("/insert_fact")
async def insert_fact(request:Home_fect,user_mail: str = Depends( JwtBearer())):    
    db = property_db()
    get_user = await get_single_user(email=user_mail)
    db["Details"].insert_one(jsonable_encoder(request))
    # it will insert limited value from the user butt all the other value vill be the same as in request body so they are initially will be 0 or null or bool
    data = db["Details"].find_one_and_update({'price':request.price,"contact_number": request.contact_number},{"$set":{"user_id":get_user["_id"]}})
    return JSONResponse(content=jsonable_encoder(propertiesEntity([data])),status_code=status.HTTP_201_CREATED)

    

@router.get("/all_pro_fact/")
async def all_pro_fact():
    db = property_db()
    data = db["Details"].find()
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/single_pro_fact/")
async def single_pro_fact(id): 

    data_pro = await get_single_property(id)
    propty: property_get.Property = property_get.Property(**data_pro[0])
    data_id = propertiesEntity(data_pro)
    actual_data = await get_complete_property(data_id,propty)

    if data_pro is not None:
        return JSONResponse(content=actual_data,status_code=status.HTTP_200_OK)

@router.delete("/delete_pro/")
async def delete_pro(id):
    db = property_db()
    db["Details"].delete_one({"_id":ObjectId(id)})
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail=f"Property deleted")

@router.put('/{id}')
def update(id,request:Home_fect):
    db = property_db()
    db["Details"].find_one_and_update({'_id':ObjectId(id)},{"$set":jsonable_encoder(request)})
    # return {"Property":"updated"}
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail=f"Property updated")



# app.mount("/static", StaticFiles(directory=os.path.join(this_directory, "static")))
@router.put("/upload/")
async def upload_images(id,files: List[UploadFile] = File(...)):
    # print(location)
    if(not os.path.exists(ROOT_PATH)):
        os.mkdir(ROOT_PATH)
    
    if(not os.path.exists(ROOT_PATH+"/images/")):
        os.mkdir(ROOT_PATH+"/images/")
        
    try:
        list_images = []
        for file in files:
            contents = file.file.read()
            completeName = os.path.join(ROOT_PATH+"/images/", file.filename) 

            with open(completeName, 'wb') as f:
                list_images.append(ROOT_PATH+"/images/"+file.filename)
                # print(list_images)
                f.write(contents)
        print(os.listdir(ROOT_PATH+"/images/"))
        db = property_db()
        await db["Details"].find_one_and_update({"_id":ObjectId(id)},{"$set":{"image_list":list_images}})
        return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}
    except:
        return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}