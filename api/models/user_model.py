from ..utils import mongoObjectId
from pydantic import BaseModel, Field, EmailStr,validator
from bson import ObjectId
from typing import Optional

class UserSchema(BaseModel):
    # id: mongoObjectId.PyObjectId = Field(default_factory=mongoObjectId.PyObjectId, alias="_id") 
    first_name: str = Field(...)
    last_name: str = Field(...)
    bio: Optional[str] = ""
    email: EmailStr = Field(...)
    password: str = Field(...)
    is_agent : bool = False
    website: Optional[str] = ""

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserUpdateSchema(BaseModel):
    bio: Optional[str] = ""

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "bio": "update your bio",
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "can@gmail.com",
                "password": "123456"
            }
        }

def userEntity(item)->dict:
    # return item
    return {
        "full_name":item["first_name"] + item["last_name"],
        "email" : item["email"],

    }

def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]


class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Student(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    