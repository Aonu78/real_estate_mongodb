from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from ..db.database import property_db
from ..crud.property import get_complete_property
from ..models import property_get
from ..models.property_get import propertiesEntity

router = APIRouter(
    tags=['Availability']
)
@router.get("/sold_property")
async def property_sold():
    db = property_db()
    data = db["Details"].find({"availability" : False,"site_type" : "sale"})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/rent_property")
async def property_rentrized():
    db = property_db()
    data = db["Details"].find({"availability" : False,"site_type" : "rent"})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/sale_available")
async def available_sale():
    db = property_db()
    data = db["Details"].find({"availability" : True,"site_type" : "sale"})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)

@router.get("/rent_available")
async def available_rent():
    db = property_db()
    data = db["Details"].find({"availability" : True,"site_type" : "rent"})
    lis = []
    for data in data:
        data_id = propertiesEntity([data])
        propty: property_get.Property = property_get.Property(**data)
        actual_data = await get_complete_property(data_id,propty)
        lis.append(actual_data)
        
    return JSONResponse(content=lis,status_code=status.HTTP_200_OK)