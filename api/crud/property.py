from ..db.database import user_db
from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse
import json
from bson import json_util

async def get_single_property(id) -> dict:
    conn = user_db()
    if id:
        db_property = conn["Details"].find({'_id':ObjectId(id)})
        print("***************************************************************1111")
        
        if db_property:
            return db_property
            # return JSONResponse(status_code=status.HTTP_200_OK, content=db_property)

async def get_complete_property(data_id,propty) -> dict:
    actual_data = {}
    actual_data["id"] = data_id[0]["id"]
    actual_data["user_id"] = str(propty.user_id)
    actual_data["price"] = propty.price
    actual_data["contact_number"] = propty.contact_number
    actual_data["site_type"] = propty.site_type
    actual_data["availability"] = propty.availability
    actual_data["general"] = propty.general
    actual_data["location"] = propty.location
    actual_data["room_details"] = propty.room_details
    actual_data["utility_details"] = propty.utility_details
    actual_data["building_details"] = propty.building_details
    # print(actual_data)
    return actual_data