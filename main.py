from fastapi import FastAPI


from api.endpoints import user_router
from api.endpoints import property_router
from api.endpoints import availability,rent,purchase

app = FastAPI(
    title="FastApi with Mongodb",
)

app.include_router(user_router.router)
app.include_router(property_router.router)
app.include_router(availability.router)
app.include_router(rent.router)
app.include_router(purchase.router)
