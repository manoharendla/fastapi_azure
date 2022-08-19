from fastapi import FastAPI
from modules.routers import (
    users,
    admins,
    home

)
app = FastAPI(title="manoapp", description="test app")

app.include_router(users.router)
app.include_router(admins.router)
app.include_router(home.router)