# from optparse import Option
from typing import Optional
from pydantic import BaseModel,HttpUrl
from bson import ObjectId
class coordinates(BaseModel):
    latitude :Optional[str] = None
    longitude : Optional[str] = None
class location(BaseModel):
    country : Optional[str] = None
    city : Optional[str] = None
    state_code : Optional[str] = None
    home_address :Optional[str] = None
    zip_code : Optional[str] = None
    coordinates : coordinates 
class bathes(BaseModel):
    full_bathe : Optional[int] = 0
    thrd_qutr : Optional[int] = 0
    half : Optional[int] = 0
    quater : Optional[int] = 0
class general(BaseModel):
    pro_owner : Optional[str] = None
    land_type : Optional[str] = None
    bath : bathes 
    unit_no : Optional[str] = None
    beds : Optional[int] = 0
    furneshed_sqr_feet : Optional[int] = 0
    lot_size : Optional[int] = 0
    year_built : Optional[int] = 0
    structure_remodel_year : Optional[int] = 0
    hoa_dues : Optional[float] = 0
    basement_sq_ft : Optional[int] = 0
    garage_sq_ft : Optional[int] = 0
    discription : Optional[str] = None
    website_link : Optional[str] = None
class appliance(BaseModel):
    dryer : Optional[bool] = False
    freezer : Optional[bool] = False
    garbage_disposal : Optional[bool] = False
    microwave : Optional[bool] = False
    range_or_oven : Optional[bool] = False
    refrigerator : Optional[bool] = False
    trash_compactor : Optional[bool] = False
    washer : Optional[bool] = False
class basement(BaseModel):
    finished : Optional[bool] = False
    partially_finished : Optional[bool] = False
    unfinished : Optional[bool] = False
    not_finished : Optional[bool] = False
class floor_covering(BaseModel):
    carpet : Optional[bool] = False
    concrete : Optional[bool] = False
    hardwood : Optional[bool] = False
    laminate : Optional[bool] = False
    linoleum_or_vinyl : Optional[bool] = False
    slate : Optional[bool] = False
    softwood : Optional[bool] = False
    tile : Optional[bool] = False
    other_type_floor : Optional[bool] = False
class rooms(BaseModel):
    breakfast_room : Optional[bool] = False
    dining_room : Optional[bool] = False
    family_room : Optional[bool] = False
    laundry_room : Optional[bool] = False
    library : Optional[bool] = False
    master_bath : Optional[bool] = False
    mud_room : Optional[bool] = False
    office : Optional[bool] = False
    pantry : Optional[bool] = False
    recreation_room : Optional[bool] = False
    workshop : Optional[bool] = False
    solarium_or_atrium : Optional[bool] = False
    sun_room : Optional[bool] = False
    walk_in_cliset : Optional[bool] = False
    total_room : Optional[int] = 0
class indore_feature(BaseModel):
    attic : Optional[bool] = False
    cable_ready : Optional[bool] = False
    ceiling_fans : Optional[bool] = False
    double_pane_or_strom_windows : Optional[bool] = False
    fireplace : Optional[bool] = False
    intercom_system : Optional[bool] = False
    jetted_tub : Optional[bool] = False
    mother_in_law_apartment : Optional[bool] = False
    security_system : Optional[bool] = False
    skylights : Optional[bool] = False
    vaulted_ceiling : Optional[bool] = False
    wet_bar : Optional[bool] = False
    wired : Optional[bool] = False
class room_details(BaseModel):
    appliance : appliance  
    basement : basement  
    floor_covering : floor_covering 
    rooms : rooms 
    indore_feature : indore_feature 
class cooling_types(BaseModel):
    central : Optional[bool] = False
    evaporative : Optional[bool] = False
    cool_geothermal : Optional[bool] = False
    refrigration : Optional[bool] = False
    solar_type : Optional[bool] = False
    wall_type : Optional[bool] = False
    other_type : Optional[bool] = False
    none_type : Optional[bool] = False
class heating_type(BaseModel):
    baseboard : Optional[bool] = False
    hot_geothermal : Optional[bool] = False
    forced_air : Optional[bool] = False
    heat_pump : Optional[bool] = False
    radiant : Optional[bool] = False
    stove : Optional[bool] = False
    heat_wall : Optional[bool] = False
    heat_other : Optional[bool] = False
class heating_fuel(BaseModel):
    coal_as_fuel : Optional[bool] = False
    electric_as_fuel : Optional[bool] = False
    gas_as_fuel : Optional[bool] = False
    oil_as_fuel : Optional[bool] = False
    propane_or_butane : Optional[bool] = False
    solar_as_fuel : Optional[bool] = False
    wood_or_pellet : Optional[bool] = False
    other_fuel : Optional[bool] = False
    none_fuel : Optional[bool] = False
class utility_details(BaseModel):
    cooling_types : cooling_types 
    heating_type : heating_type 
    heating_fuel : heating_fuel 
class building_amenities(BaseModel):
    assisted_living_community : Optional[bool] = False
    basketball_court : Optional[bool] = False
    controlled_access : Optional[bool] = False
    disabled_access : Optional[bool] = False
    doorman : Optional[bool] = False
    elevator : Optional[bool] = False
    fitness_center : Optional[bool] = False
    gated_entry : Optional[bool] = False
    near_transportation : Optional[bool] = False
    over_55_active_community : Optional[bool] = False
    sports_cort : Optional[bool] = False
    storage : Optional[bool] = False
    tennis_court : Optional[bool] = False
class architectural_style(BaseModel):
    bungalow : Optional[bool] = False
    cape_cod : Optional[bool] = False
    colonial : Optional[bool] = False
    contemporary : Optional[bool] = False
    craftsman : Optional[bool] = False
    french : Optional[bool] = False
    georgem : Optional[bool] = False
    loft : Optional[bool] = False
    modern : Optional[bool] = False
    queen_anne_or_victorian : Optional[bool] = False
    ranch_or_rambler : Optional[bool] = False
    santa_fe_or_pueblo_style : Optional[bool] = False
    spanish : Optional[bool] = False
    split_level : Optional[bool] = False
    tudor : Optional[bool] = False
    other_architect : Optional[bool] = False
class exterior(BaseModel):
    brick : Optional[bool] = False
    cement_or_concrete : Optional[bool] = False
    composition : Optional[bool] = False
    metal : Optional[bool] = False
    shingle : Optional[bool] = False
    stone : Optional[bool] = False
    stucco : Optional[bool] = False
    vinyl : Optional[bool] = False
    wood : Optional[bool] = False
    wood_products : Optional[bool] = False
    other_exterior : Optional[bool] = False
    floor_no : Optional[int] = 0
    no_of_unite : Optional[int] = 0
class outdoor_amenites(BaseModel):
    balcony_or_patio : Optional[bool] = False
    barbecue_are : Optional[bool] = False
    deck : Optional[bool] = False
    dock : Optional[bool] = False
    fenced_yard : Optional[bool] = False
    gardon : Optional[bool] = False
    greenhouse : Optional[bool] = False
    hot_tub_or_spa : Optional[bool] = False
    lawn : Optional[bool] = False
    pond : Optional[bool] = False
    pool : Optional[bool] = False
    porch : Optional[bool] = False
    rv_parking : Optional[bool] = False
    sauna : Optional[bool] = False
    sprinkler : Optional[bool] = False
    waterfront : Optional[bool] = False
    no_of_stories : Optional[int] = 0
class parking(BaseModel):
    carport : Optional[bool] = False
    garage_attached : Optional[bool] = False
    garage_detached : Optional[bool] = False
    off_street : Optional[bool] = False
    on_street : Optional[bool] = False
    no_parking : Optional[bool] = False
    no_of_parking_spaces : Optional[int] = 0
class roof(BaseModel):
    asphalt_roof : Optional[bool] = False
    built_up_roof : Optional[bool] = False
    composition_roof : Optional[bool] = False
    metal_roof : Optional[bool] = False
    shake_or_shingle : Optional[bool] = False
    slate_roof : Optional[bool] = False
    tile_roof : Optional[bool] = False
    other_roof : Optional[bool] = False
class view(BaseModel):
    city_site : Optional[bool] = False
    mountain : Optional[bool] = False
    park : Optional[bool] = False
    territorial : Optional[bool] = False
    water : Optional[bool] = False
    none_view : Optional[bool] = False
class building_details(BaseModel):
    building_amenities : building_amenities 
    architectural_style : architectural_style 
    exterior : exterior 
    outdoor_amenites : outdoor_amenites 
    parking : parking 
    roof : roof  
    view : view 
class Home_fect(BaseModel):
    price : Optional[float] = 0.0
    availability : Optional[bool] = True
    contact_number : Optional[int] = 0
    site_type : Optional[str] = None
    general : general 
    location : location 
    ## room details
    room_details : room_details 
    # applience
    # basement
    #floor covering
    # rooms
    #  indore feature
    ## utility details
    utility_details : utility_details
    # cooling types  
    # heating type
    # heating fuel
    ## building details
    building_details : building_details
    ## building amenities
    # architectural style
    # exterior
    # outdoor amenites
    # parking
    # roof
    # view
    # contact number
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}