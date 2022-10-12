from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

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

class precise(BaseModel):
        lat: float
        lng: float

class location(BaseModel):
    location: List[precise]
    accuracy : int = 120

class city_location(BaseModel):
    city: str
    state_code : str
    postal_code: int

def propertyEntity(item)->dict:
    # return item
    return {
        
        "id":str(item["_id"]),
        # "user_id" : str(str(item["user_id"])),
        # "price" : item["price"],
        # "availability":item["availability"],
        # "contact_number" : item["contact_number"],
        # "general" : dict[item["general"]],
        # # "pro_owner" : item["pro_owner"],
        # "site_type" : item["site_type"],
        # "land_type" : item["land_type"],
        # "country" : item["country"],
        # "state_code" : item["state_code"],
        # "city" : item["city"],
        # "home_address" :item["home_address"], 
        # "zip_code" : item["zip_code"],
        # "unit_no" : item["unit_no"],
        
        # "beds" : item["beds"],
        # "full_bathe" : item["full_bathe"],
        # "thrd_qutr" : item["thrd_qutr"],
        # "half" : item["half"],
        # "quater" : item["quater"],
        # "furneshed_sqr_feet" : item["furneshed_sqr_feet"],
        # "lot_size" : item["lot_size"],
        # "year_built" : item["year_built"],
        # "structure_remodel_year" : item["structure_remodel_year"],
        # "hoa_dues" : item["hoa_dues"],
        # "basement_sq_ft" : item["basement_sq_ft"],
        # "garage_sq_ft" : item["garage_sq_ft"],
        # "discription" : item["discription"],
        # "website_link" : item["website_link"],
        # ## room details
        # # applience
        # "dryer" : item["dryer"],
        # "freezer" : item["freezer"],
        # "garbage_disposal" : item["garbage_disposal"],
        # "microwave" : item["microwave"],
        # "range_or_oven" : item["range_or_oven"],
        # "fefrigerator" : item["fefrigerator"],
        # "trash_compactor" : item["trash_compactor"],
        # "washer" : item["washer"],
        # # basement
        # "finished" : item["finished"],
        # "partially_finished" : item["partially_finished"],
        # "unfinished" : item["unfinished"],
        # "not_finished" : item["not_finished"],
        # #floor covering
        # "carpet" : item["carpet"],
        # "concrete" : item["concrete"],
        # "hardwood" : item["hardwood"],
        # "laminate" : item["laminate"],
        # "linoleum_or_vinyl" : item["linoleum_or_vinyl"],
        # "slate" : item["slate"],
        # "softwood" : item["softwood"],
        # "tile" : item["tile"],
        # "other_type_floor" : item["other_type_floor"],
        # # rooms
        # "breakfast_room" : item["breakfast_room"],
        # "dining_room" : item["dining_room"],
        # "family_room" : item["family_room"],
        # "laundry_room" : item["laundry_room"],
        # "library" : item["library"],
        # "master_bath" : item["master_bath"],
        # "mud_room" : item["mud_room"],
        # "office" : item["office"],
        # "pantry" : item["pantry"],
        # "recreation_room" : item["recreation_room"],
        # "workshop" : item["workshop"],
        # "solarium_or_atrium" : item["solarium_or_atrium"],
        # "sun_room" : item["sun_room"],
        # "walk_in_cliset" : item["walk_in_cliset"],
        # "total_room" : item["total_room"],
        # #  indore feature
        # "attic" : item["attic"],
        # "cable_ready" : item["cable_ready"],
        # "ceiling_fans" : item["ceiling_fans"],
        # "double_pane_or_strom_windows" : item["double_pane_or_strom_windows"],
        # "fireplace" : item["fireplace"],
        # "intercom_system" : item["intercom_system"],
        # "jetted_tub" : item["jetted_tub"],
        # "mother_in_law_apartment" : item["mother_in_law_apartment"],
        # "security_system" : item["security_system"],
        # "skylights" : item["skylights"],
        # "vaulted_ceiling" : item["vaulted_ceiling"],
        # "wet_bar" : item["wet_bar"],
        # "wired" : item["wired"],
        # ## utility details
        # # cooling types
        # "central" : item["central"],
        # "evaporative" : item["evaporative"],
        # "cool_geothermal" : item["cool_geothermal"],
        # "refrigration" : item["refrigration"],
        # "solar_type" : item["solar_type"],
        # "wall_type" : item["wall_type"],
        # "other_type" : item["other_type"],
        # "none_type" : item["none_type"],
        # # heating type
        # "baseboard" : item["baseboard"],
        # "hot_geothermal" : item["hot_geothermal"],
        # "forced_air" : item["forced_air"],
        # "heat_pump" : item["heat_pump"],
        # "radiant" : item["radiant"],
        # "stove" : item["stove"],
        # "heat_wall" : item["heat_wall"],
        # "heat_other" : item["heat_other"],
        # # heating fuel
        # "coal_as_fuel" : item["coal_as_fuel"],
        # "electric_as_fuel" : item["electric_as_fuel"],
        # "gas_as_fuel" : item["gas_as_fuel"],
        # "oil_as_fuel" : item["oil_as_fuel"],
        # "propane_or_butane" : item["propane_or_butane"],
        # "solar_as_fuel" : item["solar_as_fuel"],
        # "wood_or_pellet" : item["wood_or_pellet"],
        # "other_fuel" : item["other_fuel"],
        # "none_fuel" : item["none_fuel"],
        # ## building details
        # ## building amenities
        # "assisted_living_community" : item["assisted_living_community"],
        # "basketball_court" : item["basketball_court"],
        # "controlled_access" : item["controlled_access"],
        # "disabled_access" : item["disabled_access"],
        # "doorman" : item["doorman"],
        # "elevator" : item["elevator"],
        # "fitness_center" : item["fitness_center"],
        # "gated_entry" : item["gated_entry"],
        # "near_transportation" : item["near_transportation"],
        # "over_55_active_community" : item["over_55_active_community"],
        # "sports_cort" : item["sports_cort"],
        # "storage" : item["storage"],
        # "tennis_court" : item["tennis_court"],
        # # architectural style
        # "bungalow" : item["bungalow"],
        # "cape_cod" : item["cape_cod"],
        # "colonial" : item["colonial"],
        # "contemporary" : item["contemporary"],
        # "craftsman" : item["craftsman"],
        # "french" : item["french"],
        # "georgem" : item["georgem"],
        # "loft" : item["loft"],
        # "modren" : item["modren"],
        # "queen_anne_or_victorian" : item["queen_anne_or_victorian"],
        # "ranch_or_rambler" : item["ranch_or_rambler"],
        # "santa_fe_or_pueblo_style" : item["santa_fe_or_pueblo_style"],
        # "spanish" : item["spanish"],
        # "split_level" : item["split_level"],
        # "tudor" : item["tudor"],
        # "other_architect" : item["other_architect"],
        # # exterior
        # "brick" : item["brick"],
        # "cement_or_concrete" : item["cement_or_concrete"],
        # "composition" : item["composition"],
        # "metal" : item["metal"],
        # "shingle" : item["shingle"],
        # "stone" : item["stone"],
        # "stucco" : item["stucco"],
        # "vinyl" : item["vinyl"],
        # "wood" : item["wood"],
        # "wood_products" : item["wood_products"],
        # "other_exterior" : item["other_exterior"],
        # "floor_no" : item["floor_no"],
        # "no_of_unite" : item["no_of_unite"],
        # # outdoor amenites
        # "balcony_or_patio" : item["balcony_or_patio"],
        # "barbecue_are" : item["barbecue_are"],
        # "deck" : item["deck"],
        # "dock" : item["dock"],
        # "fenced_yard" : item["fenced_yard"],
        # "gardon" : item["gardon"],
        # "greenhouse" : item["greenhouse"],
        # "hot_tub_or_spa" : item["hot_tub_or_spa"],
        # "lawn" : item["lawn"],
        # "pond" : item["pond"],
        # "pool" : item["pool"],
        # "porch" : item["porch"],
        # "rv_parking" : item["rv_parking"],
        # "sauna" : item["sauna"],
        # "sprinkler" : item["sprinkler"],
        # "waterfront" : item["waterfront"],
        # "no_of_stories" : item["no_of_stories"],
        # # parking
        # "carport" : item["carport"],
        # "garage_attached" : item["garage_attached"],
        # "garage_detached" : item["garage_detached"],
        # "off_street" : item["off_street"],
        # "on_street" : item["on_street"],
        # "no_parking" : item["no_parking"],
        # "no_of_parking_spaces" : item["no_of_parking_spaces"],
        # # roof
        # "asphalt_roof" : item["asphalt_roof"],
        # "built_up_roof" : item["built_up_roof"],
        # "composition_roof" : item["composition_roof"],
        # "metal_roof" : item["metal_roof"],
        # "shake_or_shingle" : item["shake_or_shingle"],
        # "slate_roof" : item["slate_roof"],
        # "tile_roof" : item["tile_roof"],
        # "other_roof" : item["other_roof"],
        # # view
        # "city_site" : item["city_site"],
        # "mountain" : item["mountain"],
        # "park" : item["park"],
        # "territorial" : item["territorial"],
        # "water" : item["water"],
        # "none_view" : item["none_view"],
        # # contact number
        

        
    }

def propertiesEntity(entity)->list:
    return [propertyEntity(item) for item in entity]

def userEntity(item)->dict:
    # return item
    return {
        "name":item["name"],
        "email" : item["email"],
        "password" : item["password"]
    }

def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]

class TokenData(BaseModel):
    email: Optional[str] = None




from bson import ObjectId

class Property(BaseModel):

    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="user_id")
    price: str
    contact_number : str
    site_type : str
    availability : bool
    general: dict
    location : dict
    room_details : dict
    utility_details : dict
    building_details : dict
    image_list : list = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        alias_priority=2 
            