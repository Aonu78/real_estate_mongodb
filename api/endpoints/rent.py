from fastapi import APIRouter
from ..db.database import property_db
from ..models.property_get import propertiesEntity
from ..crud.property import get_complete_property
from fastapi.responses import JSONResponse
from fastapi import status
from ..models import property_get
router = APIRouter(
    tags=['rent near by zip_code/city/state'],
    prefix="/rent"
)
@router.get("/rent_by_zip")
async def property_by_zip(zipcode:str):
    db = property_db()
    # data = db["Details"].find({"zip_code" : zipcode,"site_type" : "rent","availability" : True,})
    data = db["Details"].find({"location.zip_code" : zipcode,"site_type" : "rent","availability" : True})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)


@router.get("/rent_by_city")
async def property_by_city(cityname:str):
    db = property_db()
    data = db["Details"].find({"location.city" : cityname,"site_type" : "rent","availability" : True})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/rent_by_state")
async def property_by_state(statename:str):
    db = property_db()
    data = db["Details"].find({"location.state_code" : statename,"site_type" : "rent","availability" : True,})
    # data = db["Details"].find({"location.zip_code" : zipcode,"site_type" : "rent","availability" : True})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/rent_by_country")
async def rent_by_country(country:str):
    db = property_db()
    data = db["Details"].find({"location.country":country,"availability" : True,"site_type" : "rent"})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)